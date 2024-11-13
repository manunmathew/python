# Django Project Overview

A **project** in Django is the overall application or website you are building. It includes the main settings and configurations that apply to the entire application. Each Django project contains settings, applications, and configurations for building web functionalities.

### Creating a Django Project
To start a new Django project, you can use the following command:
```plaintext
django-admin startproject projectname
```

### Django Settings
The **Django settings file** contains all the configurations for your Django installation. This file is essential as it manages the settings for your project, including database configurations, static files, templates, and installed applications.

### WSGI and ASGI
- **WSGI (Web Server Gateway Interface)**: This is a specification for a simple and universal interface between web servers and web applications or frameworks written in Python.
- **ASGI (Asynchronous Server Gateway Interface)**: The successor to WSGI, designed to handle asynchronous capabilities. It provides a standard interface between async-capable Python web servers, frameworks, and applications.

### Essential `manage.py` Commands
The `manage.py` script is a command-line utility that lets you interact with your Django project in various ways. Here are some essential commands:

- **makemigrations**: Detects changes made in your model definitions and creates migration files.
    ```plaintext
    python manage.py makemigrations
    ```

- **migrate**: Applies the migrations (i.e., changes) made in your model definitions to the database.
    ```plaintext
    python manage.py migrate
    ```

- **runserver**: Starts the development server to run and test your project locally.
    ```plaintext
    python manage.py runserver
    ```

### Default Database: SQLite3
**SQLite3** is the default database for Django applications. It's a lightweight, file-based database that's ideal for development and small projects. However, for larger projects, you might consider switching to a more robust database like PostgreSQL or MySQL.
