# API_Yatube
### RESTful-сервис для социальной сети [Yatube](https://github.com/eduvxn/hw05_final)

Реализован программный интерфейс для социальной сети со всеми типами запросов: GET, POST, PATCH, PUT, DELETE (к части требуются permissions).

### Запуск проекта:

1. Клонировать репозиторий и перейти в него в командной строке:

``` bash
git clone https://github.com/eduvxn/api_final_yatube.git
```

``` bash
cd api_final_yatube
```

2. Cоздать и активировать виртуальное окружение:

``` bash
python3 -m venv env
```

``` bash
source venv/bin/activate # для Linux
```

``` bash
source venv/bin/activate # для Windows
```

``` bash
python3 -m pip install --upgrade pip
```

3. Установить зависимости из файла requirements.txt:
 
``` bash
pip install -r requirements.txt
```

4. Выполнить миграции:

``` bash
python3 manage.py migrate
```

5. Запустить проект:

``` bash
python3 manage.py runserver
```

## Технологии

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django REST framework](https://www.django-rest-framework.org/)
* [DRF Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
