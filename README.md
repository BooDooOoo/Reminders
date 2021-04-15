# Reminders
 Web-application to create short reminders
 
 
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
* [Redis](https://rometools.github.io/rome/) - Task broker
