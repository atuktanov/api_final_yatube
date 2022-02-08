## Проект «API для Yatube»

### Описание:
Это учебный проект по теме API: интерфейс взаимодействия программ курса Python-разработчик плюс в Яндекс Практикуме.

Проект представляет из себя API для блог-платформы Yatube, созданный на основе Django REST Framework.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/atuktanov/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Как работать с API:

Документация к API в формате ReDoc доступна по адресу http://127.0.0.1:8000/redoc/ после запуска проекта