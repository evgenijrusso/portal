 Создание проекта
 -------------------
1. создал каталог 'portal'. Там уже по умолчанию указан интерпретатор Python  3.11 и poetry executable (location) - `C:\Users\rasen\AppData\Roaming\pypoetry\venv\Scripts\poetry.exe`
2. `poetry init --no-interaction --dependency django` => create file pyproject.toml  (пропустил)
3. `poetry run django-admin startproject NewsPortal` => create file manage.py and another files
4. `poetry install` - install django and ..., poetry.lock
5. Активизация GIT: VSC -> Enable Version Control Integration, в выпадающем меню выбираем Git
6. cd NewsPortal и `python manage.py migrate` - Ok (первичные миграции). 
7. Отказался от того, чтобы в git контролировать внешние библиотеки
8. Первый коммит  
9. `python manage.py runserver` - Ok
10. Настроил конфигурцию запуска проектв через порт 8004
11. Изменил рабочаю папку проекта (теперь 'work')
12. Создал новое приложение `news` (python manage.py startapp news)
13. Добавил модели и миграции, соединился с БД (sqlite).

### Подготовьте файл, в котором напишете список всех команд, запускаемых в Django shell.
файл - `NewsPortal/news/forRead/notes.md`
--------------------------

14. Создал `templates` не в корне проекта, а в приложении `news`. Далее создал представления на основе моделей
15. Создал суперпользователя: `python manage.py createsuperuser` (admin-1)
16. Добавил страницу "Новости" (список новостей, posts.html) и отдельную отдельную страницу 
для полной информации о статье (post.html)
17. Загрузил пакет allauth.
У allauth адреса регистрации и авторизации вот такие:
http://127.0.0.1:8000/accounts/signup/
http://127.0.0.1:8000/accounts/login/