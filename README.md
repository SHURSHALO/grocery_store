# Sarafan

> Sarafan** — это веб-приложение для управления продуктами и корзиной покупок. Этот проект предоставляет пользователям возможность просматривать товары, добавлять их в корзину, а также управлять своими заказами в интернет-магазине.

## Содержание

- [Описание](#описание)
- [Функциональность](#функциональность)
- [Технологии](#технологии)
- [Установка и запуск](#установка-и-запуск)

## Описание

Sarafan предназначен для упрощения процесса управления товарами и корзиной покупок в интернет-магазине. Пользователи могут просматривать доступные товары, добавлять их в корзину, изменять количество и удалять товары из корзины. Приложение также включает административную панель для управления товарами и заказами.

## Функциональность

- **Управление товарами:**
  - Просмотр списка товаров.
  - Просмотр списка категорий и подкатегорий.

- **Корзина покупок:**
  - Добавление товаров в корзину.
  - Изменение количества товаров.
  - Удаление товаров из корзины.
  - Очистка всей корзины.

- **Управление пользователями:**
  - Вход в систему.
  - Выход из системы.
  - Управление корзиной и заказами только для авторизованных пользователей.

- **Административная панель:**
  - Управление товарами и категориями.
  - Просмотр, удаление и редактирование заказов.

## Технологии

- **Django:** Основной фреймворк для разработки веб-приложения.
- **Bootstrap:** Используется для стилизации и создания адаптивного дизайна.
- **Python Decouple:** Для безопасного управления конфигурацией через переменные окружения.
- **Pillow:** Для обработки изображений, включая изменение размеров и форматов.

## Установка и запуск

1. Клонируйте репозиторий:
    ```bash
    git clone git@github.com:SHURSHALO/sarafan.git
    ```
2. Перейдите в директорию проекта:
    ```bash
    cd sarafan
    ```
    
3. Создайте `.env` по примеру `.env.example`
  
4. Создайте и активируйте виртуальное окружение:
    ```bash
    py -3.9 -m venv venv

    source venv/Scripts/activate  # Для Windows
    ```
5. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
6. Выполните миграции базы данных:
    ```bash
    cd sarafan
    python manage.py migrate
    ```
7. Создайте суперюзера:
   ```bash
   python manage.py createsuperuser
   ```
8. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

Заполните БД

Теперь вы можете открыть веб-браузер и перейти по адресу http://127.0.0.1:8000/products/categories/ для просмотра приложения.

Админка по адресу: http://127.0.0.1:8000/admin/
