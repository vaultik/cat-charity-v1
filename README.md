## Summary: ##
    Привет! 
_Данный проект - благотворительный фонд поддержки котиков QRKot._ 

**Проект написан на фреймворке FastAPI, модели - SQLAlchemy, миграции - Alembic, валидация - Pydantic.**

**Функции:**

_1) Можно создавать благотворительные проекты с необходимой суммой для инвестиций._

_2) Можно отправлять пожертвования, которые автоматически инвестируются в проекты от старых к новым (FIFO)._

_Даже имеются необходимые тесты на pytest!!!_

_Проект будет полезен тем, кто изучает FastAPI, SQLAlchemy, Alembic и Pydantic. В общем - пользуйтесь, кому понадобится!)_

---

## Стек основных технологий: ##

- **Python 3.9**
- **FastAPI 0.111.0**
- **SQLAlchemy 2.0.29**
- **Alembic 1.7.7**
- **Pydantic 2.7.1**
- **pytest 7.1.3**

Список необходимых зависимостей см. в (requirements.txt)

---

## **_Как запустить проект:_** ##

**_Клонировать репозиторий и перейти в него в командной строке:_**

    git clone https://github.com/Marakes/cat-charity-1

    cd cat-charity-1

**_Cоздать и активировать виртуальное окружение:_**

    python3 -m venv venv

  * Если у вас Linux/macOS

        source venv/bin/activate

  * Если у вас windows

        source venv/scripts/activate

**_Установить зависимости из файла requirements.txt:_**

    python3 -m pip install --upgrade pip
    pip install -r requirements.txt

**_Запуск сервеса:_**

    uvicorn app.main:app --reload

**_Перейти на API документацию Swagger:_**

    http://127.0.0.1:8000/docs

## **_Примеры запросов и ответы:_** ##

**_POST запрос на создание проекта:_**

    {
      "name": "WowWow",
      "description": "Needs moreee",
      "full_amount": 1000
    }


**_Ответ со статусом 200:_**

    {
      "name": "WowWow",
      "description": "Needs moreee",
      "full_amount": 1000,
      "id": 3,
      "invested_amount": 0,
      "fully_invested": false,
      "create_date": "2025-12-19T17:21:24.032248"
    }

**_GET запрос на получение списка пожертвований:_**

    [
      {
        "full_amount": 100,
        "comment": "string",
        "id": 1,
        "create_date": "2025-12-19T16:43:21.311806",
        "invested_amount": 100,
        "fully_invested": true,
        "close_date": "2025-12-19T16:43:21.322164"
      },
      {
        "full_amount": 30,
        "comment": "string",
        "id": 2,
        "create_date": "2025-12-19T16:46:31.380712",
        "invested_amount": 30,
        "fully_invested": true,
        "close_date": "2025-12-19T16:46:31.416814"
      },
      {
        "full_amount": 20,
        "comment": "string",
        "id": 3,
        "create_date": "2025-12-19T16:46:35.087279",
        "invested_amount": 20,
        "fully_invested": true,
        "close_date": "2025-12-19T16:46:35.093384"
      }
    ]


## Автор проекта: ##

Невероятный и непревзойдённый (как и все) студент Яндекс Практикума :)

https://github.com/Marakes
