# API для Yatube
Это учебный проект по теме API: интерфейс взаимодействия программ курса Python-разработчик плюс в Яндекс Практикуме.
Проект представляет из себя API для блог-платформы Yatube, созданный на основе Django REST Framework.

## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
- [Над проектом работали](#над-проектом-работали)

## Технологии
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

## Использование
Склонируйте репозиторий  
Создайте виртуальное окружение 
```
python -m venv venv
```
Активируйте виртуальное окружение  
Установить зависимости 
```
pip install -r requirements.txt
```
Выполните миграции:
```
python manage.py migrate
```
Запустите проект:
```
python manage.py runserver
```
Документация к API в формате ReDoc доступна по адресу http://127.0.0.1:8000/redoc/ после запуска проекта


## Над проектом работали

- [Алексей Туктанов](https://t.me/atuktanov)
