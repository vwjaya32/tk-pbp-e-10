release: sh -c 'python manage.py migrate'
web: python manage.py migrate && gunicorn project_django.wsgi
