# db-hack

Этот скрипт предназначен для исправления оценок и замечаний учителя в базе данных электронного дневника. 
Вам достаточно запустить в Django shell соответствующую функцию и передать ей имя ученика.
Кроме этого, скрипт может добавлять похвалы от учителей по выбранным предметам.

## Запуск

Для работы скрипта вам понадобится копия сайта электронного дневника, установленная на вашем компьютере, и подключенная база данных:
- Скачайте код сайта электронного дневника школы из репозитория [e-diary](https://github.com/devmanorg/e-diary/tree/master).
- Установите и запустите свою копию сайта. [Документация](https://github.com/devmanorg/e-diary/tree/master#%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA)
содержит необходимые инструкции. 
- [Настройте переменные окружения](https://github.com/devmanorg/e-diary/tree/master#%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F)
, указав секретный ключ проекта и путь к базе данных дневника.
- Загрузите файл `scriprs.py` из репозитория [db-hack](https://github.com/Tenundor/db-hack) на ваш сервер в каталог сайта (в ту же папку, где находится файл manage.py).
- Откройте терминал и перейдите в каталог сайта.
- При необходимости, активируйте окружение проекта:
  - Windows: ``.\venv\Scripts\activate``
  - MacOS/Linux: ``source venv/bin/activate``
- Запустите Django shell:
```shell
python manage.py shell
```
- Импортируйте функции из файла `script.py` командой `import`:
```python
from script import fix_marks, remove_chastisements, create_commendation
```

## Исправление плохих оценок и замечаний учителя

Для исправления двоек и троек на пятёрки вызовите в Django shell импортированную функцию `fix_marks`, указав в качестве аргумента фамилию и имя ученика:
```python
fix_marks("Фамилия Имя")
```
Для удаления замечаний учителя вызовите функцию `remove_chastisements`, также указав имя ученика:
```python
remove_chastisements("Фамилия Имя")
```

## Добавление похвалы учителя

Вызовите в Django shell функцию `create_commendation`, указав в качестве аргументов полное имя ученика и название предмета с большой буквы:
```python
create_commendation("Фамилия Имя", "Предмет")

```
## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

