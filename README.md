# Reminders
 Web-application to create short reminders

## Description

User:
* must register and login
* can create, update and delete reminder
* will receive email with reminder in time
 
## Installing

You can deploy this project using docker

Copy this repository on your local machine

Enter your secret key in secret-key.env

For example you can generate it on [Djecrety.ir](https://djecrety.ir/) or use command
```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

In email-variables.env configure your SMTP settings

Use the following command in the project folder on your local machine

```
docker-compose up
```

## Built With

* [Django](https://docs.djangoproject.com/en/3.2/) - The web framework used
* [Celery](https://docs.celeryproject.org/en/stable/) - Task manager
* [Redis](https://redis.io/) - Task broker
* [Docker](https://www.docker.com/) - Deliver software in packages

## Preview

https://user-images.githubusercontent.com/42356579/114954114-7d3c0080-9e62-11eb-91cf-e044b003fb09.mp4