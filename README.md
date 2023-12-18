# Создание проекта
1. создал каталог 'portal'. Там уже по умолчанию указан интерпретатор Python  3.11 и poetry executable (location) - `C:\Users\rasen\AppData\Roaming\pypoetry\venv\Scripts\poetry.exe`
2.  `poetry init --no-interaction --dependency django` => create file pyproject.toml  (пропустил)
3.  `poetry run django-admin startproject NewsPortal` => create file manage.py and another files
4.  `poetry install` - install django and ..., poetry.lock
5.  Активизация GIT: VSC -> Enable Version Control Integration, в выпадающем меню выбираем Git
6.  cd NewsPortal и `python manage.py migrate` - Ok (первичные миграции). 
7.  Отказался от того, чтобы в git контролировать внешние библиотеки
8.  Первый коммит  
9. `python manage.py runserver` - Ok
10. Настроил конфигурцию запуска проектв через порт 8004
