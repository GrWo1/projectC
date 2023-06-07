# CHOOGLE (поиск)
[Открыть проект](http://185.105.90.22/)

## Описание

Проект на фреймворке Django для поска по ключевым словам на [сайте](https://bkrs.info/)

## Установка

1. Склонируйте репозиторий на локальную машину:

   ```
   git clone https://github.com/GrWo1/projectC.git
   ```
2. Установите виртуальное окружение venv:
    ```
    python3 -m venv venv
   или
    python -m venv venv
    ```
3. Запустити виртуальное окружение:
    ```
    source venv/bin/activate (Linux/MacOS)
    ```
4. Установите зависимости:
    ```
    pip install -r requirements.txt
    ```
5. Перейдите в папку проекта:

    ```
    cd search/
    ```

6. Выполните миграции базы данных:

   ```
   python manage.py migrate
   ```

7. Запустите локальный сервер:

   ```
   python manage.py runserver
   ```

8. Откройте веб-браузер и перейдите по адресу [http://localhost:8000/](http://localhost:8000/) для доступа к приложению.
