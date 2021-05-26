# API для проекта Yatube на базе Django Rest Framework. Приложение предосталвяет удобный доступ к данным проекта Yatube.

# Требования:
* Python 3.7+

# Начало работы:
* Склонируйте репозиторий api_final_yatube
git clone https://github.com/pichugina-v/api_final_yatube.git
* Установите зависимости
pip install -r requirements.txt
* Запустите приложение
python manage.py runserver

# Аутентификация:
В проекте реализована JWT аутентификация. Для получения access token и refresh token отправье POST-запрос на адрес http://127.0.0.1:8000/api/v1/token/
В запросе передайте 
```
username: <username> 
password: <password>
```

Для аутентификации при отправке запроса передавайте токен в заголовке 
```
Authorization: Bearer <access token>
```

Для обновления токена отправьте POST-запрос на адрес http://127.0.0.1:8000/api/v1/token/refresh/
В запросе передайте
```
refresh: <refresh token>
```

Access token действителен в течение 30 дней, resresh token - в течение 90 дней
Вы можете самостоятельно изменить срок действия access token и refresh token в настройках проекта. Для этого в /yatube_api/settings.py измените значения в строках
```
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=90)
}
```

# Функционал:
Приложение предоставляет возможность получать информацию о:
* Всех постах
* Всех группах
* Постах в определенной группе
* Определенном посте
* Коментариях к определенному посту
* Конкретном комментарии к определенному посту
* Ваших подписках

*Информация о подписках поступна только аутентифицированным клиентам.*

# Примеры использования:

