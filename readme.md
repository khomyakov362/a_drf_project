# A Django Rest Framework Rroject

## Description

This is a DRF project created for the purposes of studying.
The project is an API that can provide quizzes on different topics.
It allows to create users with different roles and restrict access to some features.

## Installation

1. Navigate to a folder and clone the repository:

```shell
    cd <your folder>
    git clone https://github.com/khomyakov362/a_drf_project.git
```
2. Create virtual environment:

```shell
    python -m venv ./venv
```

4. Activate venv:

For Linux:
```shell
    source venv/bin/activate
```

For Windows Powershell:
```shell
    .venv/bin/activate
```

5. Instal requirements:

For Linux:
```shell
    pip install -r requirements.txt
```

6. Create .env file in the root directory based on .env_sample.

7. When run on Windows with MCSQL run command to create database:

```shell
    python manage.py ccdb
```

8. Run the following commands to migrate to the database:

```shell
    python manage.py makemigrations
    python manage.py migrate
```

9. Create sample users:

```shell
    python manage.py ccsu
```

10. Run server:

```shell
    python manage.py runserver
```

11. Access server through your browser or Postman.

12. Read automatically generated documentation at /swagger/ or /redoc/
