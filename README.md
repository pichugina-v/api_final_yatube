# API для проекта Yatube на базе Django Rest Framework. Приложение предосталвяет удобный доступ к данным проекта Yatube.


# Начало работы:
* Склонируйте репозиторий `api_final_yatube`
```python
git clone https://github.com/pichugina-v/api_final_yatube.git
```
* Установите зависимости
```python
pip install -r requirements.txt
```
* Создайте модели и выполните миграции
```python
python manage.py makemigrations
python manage.py migrate
```
* Запустите приложение
```python
python manage.py runserver
```


# Аутентификация:
В проекте реализована JWT аутентификация. Для получения `access token` и `refresh token` отправье POST-запрос на адрес http://127.0.0.1:8000/api/v1/token/
В запросе передайте
```python
username: <username> 
password: <password>
```


Для аутентификации при отправке запроса передавайте токен в заголовке 
```python
Authorization: Bearer <access token>
```


Для обновления токена отправьте POST-запрос на адрес http://127.0.0.1:8000/api/v1/token/refresh/
В запросе передайте
```python
refresh: <refresh token>
```

`Access token` действителен в течение 30 дней, `resresh token` - в течение 90 дней
Вы можете самостоятельно изменить срок действия `access token` и `refresh token` в настройках проекта. Для этого в `/yatube_api/settings.py` измените значения в строках
```python
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=90)
}
```


# Функционал:
Приложение предоставляет возможность:
* Создавать, читать, изменять, удалять посты
* Создавать, читать, изменять, удалять группы
* Создавать, читать, изменять, удалять комментарии к постам
* Подписываться на пользователей
* Получать список подписчиков

*Доступ к подпискам доступен только для аутентифицированных клиентов. Для остальных объектов неаутентифицированным клиентам доспутна только функция чтения (GET).*


# Доступные url:
* /api/v1/posts/
* /api/v1/posts/{post_id}/
* /api/v1/posts/{post_id}/comment/
* /api/v1/posts/{post_id}/comment/{comment_id}/
* /api/v1/group/
* /api/v1/follow/


# Примеры использования:
* Для чтения информации необходимо отправить GET-запрос на адрес http://127.0.0.1:8000/api/v1/posts/. Запрос вернет данные о всех постах
```python
[
    {
        "id": 2,
        "author": "admin",
        "text": "Two",
        "pub_date": "2021-05-26T08:53:27.632327Z",
        "group": null
    },
    {
        "id": 1,
        "author": "admin",
        "text": "One",
        "pub_date": "2021-05-26T08:53:03.277467Z",
        "group": null
    }
]
```

* Для создания нового поста отправьте POST-запрос на адрес http://127.0.0.1:8000/api/v1/posts/. В запросе обязательно передать
```python
text: <text>
```
* Для изменения поста отправьте PUT-запрос на адрес http://127.0.0.1:8000/api/v1/posts/{post_id}/. В запросе обязательно передать
```python
text: <text>
```
* Для частичного изменения поста отправьте PATCH-запрос на адрес http://127.0.0.1:8000/api/v1/posts/{post_id}/
* Для частичного изменения поста отправьте DELETE-запрос на адрес http://127.0.0.1:8000/api/v1/posts/{post_id}/
* Для фильтрации постов по группе отправьте GET-запрос http://127.0.0.1:8000/api/v1/posts/ , указав в `params`
```python
group: <group_id>
```
