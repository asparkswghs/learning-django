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

1. Create and config templates dir
    - `mkdir <projname>/<appname>/templates/` (i.e. inside the app folder)
    - Edit `<projname>/<projname>/settings.py`
        ```python
        TEMPLATES = [
            {
                ...,
                'DIRS': [
                    [BASE_DIR / 'templates'] # Add this line
                ],
                ...,
            },
        ]

#### Creating pages
1. Create a file in templates dir from before, named `<pagename>.html`

1. Create a function to load it, in `<projname>/<appname>/views.py`
    ```python
    # Add a function like this, after the comment
    def page_name(request):
        context = {
            ...
        }
        return render(request, '<pagename>.html', context)
    ```

1. Add urls:
    - Create `<projname>/<appname>/urls.py` if it doesn't exist
    - Add the following for your app to `<projname>/<projname>/urls.py` if you haven't already:
        ```python
        ...
        from django.urls import path, include # add the ', include' bit here
        urlpatterns = [
            ...,
            path('', include('<appname>.urls'))
        ]

    - Edit `<projname>/<appname>/urls.py`:
        ```python
        from django.urls import path
        from . import views

        urlpatterns = [
            path('/base', views.base, name='base')
        ]
        ```


