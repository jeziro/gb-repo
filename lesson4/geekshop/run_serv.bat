@ECHO OFF

start cmd.exe /k "D:\pycharm\django_st1\venv\Scripts\activate & cd /d D:\pycharm\django_st1\lesson1\geekshop & python manage.py runserver"
start C:\"Program Files (x86)"\Google\Chrome\Application\chrome.exe "http://127.0.0.1:8000/"