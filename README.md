# Learning Django!

#### Run (Development Server)

```bash
# Get the source code
git clone https://github.com/asparkswghs/learning-django

cd learning-django/learning

# Run the Development Server
./manage.py runserver
```

#### Development

1. Create venv
    ```bash
    python -m venv .venv
    ```

1. Enter venv
    ```bash
    # Real operating systems (yay POSIX!)
    source .venv/bin/activate

    # Windows (mingw64)
    source .venv/Scripts/activate
    ```

1. Install Requirements
    ```bash
    pip install -r requirements.txt
    ```

1. To update deps, use the following command
    ```bash
    pip freeze > requirements.txt
    ```