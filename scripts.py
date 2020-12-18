from datacenter.models import Schoolkid, Lesson, Mark, Chastisement, Commendation
import random


def get_schoolkid(schoolkid_name):
    if not schoolkid_name:
        raise ValueError("Вы не указали имя ученика.")
    try:
        return Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.DoesNotExist:
        raise ValueError(
            f"Ученик с именем {schoolkid_name} не найден. Проверьте правильность написания имени."
        ) from None
    except Schoolkid.MultipleObjectsReturned:
        raise ValueError(
            f"Существует несколько учеников с именем {schoolkid_name}. Уточните запрос"
        ) from None


def fix_marks(schoolkid_name):
    try:
        schoolkid = get_schoolkid(schoolkid_name)
    except ValueError as argument_value_error:
        return str(argument_value_error)
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
    for mark in bad_marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid_name):
    try:
        schoolkid = get_schoolkid(schoolkid_name)
    except ValueError as argument_value_error:
        return str(argument_value_error)
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def get_subject_lessons_without_commendations(schoolkid, subject_title):
    if not subject_title:
        raise ValueError("Вы не указали школьный предмет.")
    subject_lessons = Lesson.objects.filter(
        subject__title=subject_title,
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
    )
    if not subject_lessons:
        raise ValueError("Школьный предмет не найден. Проверьте название предмета.")
    existing_commendations = Commendation.objects.filter(
        schoolkid=schoolkid,
        subject__title=subject_title,
    )
    existing_commendations_dates = [
        existing_commendation.created for existing_commendation in existing_commendations
    ]
    return subject_lessons.exclude(
        date__in=existing_commendations_dates
    )


def create_commendation(schoolkid_name, subject_title):
    commendation_variants = [
        "Молодец!", "Отлично!", "Хорошо!", "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!", "Великолепно!", "Прекрасно!", "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!", "Сказано здорово - просто и ясно!",
        "Ты, как всегда, точен!", "Очень хороший ответ!",
    ]
    try:
        schoolkid = get_schoolkid(schoolkid_name)
        last_lesson_without_commendation = get_subject_lessons_without_commendations(
            schoolkid,
            subject_title,
        ).order_by("-date").first()
    except ValueError as argument_value_error:
        return str(argument_value_error)
    random_commendation = random.choice(commendation_variants)
    Commendation.objects.create(
        text=random_commendation,
        created=last_lesson_without_commendation.date,
        schoolkid=schoolkid,
        subject=last_lesson_without_commendation.subject,
        teacher=last_lesson_without_commendation.teacher,
    )
