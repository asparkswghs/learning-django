# Notes!

## Django project

#### Setup
```sh
# Create project
django-admin startproject <projname>

# Change directories
cd <projname>

# Create app
django-admin startapp <appname>

# Run server
./manage.py runserver

# Build database
./manage.py migrate

# Create super user
./manage.py createsuperuser
```
#### Development
1. Install your app
    - Edit `<projname>/<projname>/settings.py`
        ```python
        INSTALLED_APPS = [
            ...,
            <appname>, # Add this line
        ]
        ```
    