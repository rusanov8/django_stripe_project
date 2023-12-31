# Django E-Commerce Project

## Описание проекта

Этот проект представляет собой веб-приложение электронной коммерции, разработанное на базе фреймворка Django. Проект включает в себя функциональности, такие как просмотр товаров, добавление их в корзину, оформление заказа и оплата товаров.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/rusanov8/django_stripe_project.git
    ```

2. Перейдите в директорию проекта:

    ```bash
    cd django_stripe_project
    ```

3. Создайте виртуальное окружение (рекомендуется использовать `venv`):

    ```bash
    python -m venv venv
    ```

4. Активируйте виртуальное окружение:

    - На Windows:

        ```bash
        venv\Scripts\activate
        ```

    - На macOS и Linux:

        ```bash
        source venv/bin/activate
        ```

5. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

6. Примените миграции:

    ```bash
    python manage.py migrate
    ```

7. Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

8. Откройте веб-браузер и перейдите по адресу http://127.0.0.1:8000/ для доступа к приложению.

## Функциональности

- **Просмотр товаров**: Пользователи могут просматривать доступные товары.

- **Добавление в корзину**: Пользователи могут добавлять товары в корзину.

- **Оформление заказа**: Пользователи могут оформлять заказы с добавленными товарами.

- **Оплата заказа**: Реализована интеграция с платежным шлюзом для оплаты оформленных заказов.

- **Управление заказами**: Пользователи могут просматривать и управлять своими заказами.

## Докеризация

Для запуска проекта с использованием Docker:

1. Постройте и запустите контейнеры:

    ```bash
    docker-compose up --build
    ```

2. Доступ к приложению по адресу http://localhost:8000/.

