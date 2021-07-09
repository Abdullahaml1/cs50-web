# Steps to operate over django

## Installation and basic setup
1. install it `pip3 instll Django`
2. to build new project `django-admin startproject your_project_name`
3. to run your project 
```bash
$ python3 your_project_name manage.py runserver`
OUTPUT:
atching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
July 08, 2021 - 22:19:13
Django version 3.2.5, using settings 'start.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```


## Adding apps
1. create the app:  

```bash
cd your project_name
pythn3 manage.y startapp your_app_name
```


2. add the new app to the project: go to the project_name/project_name/settings.py file and add the new app into `INSTALLED_APPS` list ex:
```python3
INSTALLED_APPS = [
    'hello'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

```


3. create function the reacts with certain request in `views.py`
```python3
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello World")
```


4. then `cd` to the app and create `urls.py` and fill it with urls coressponds what to respnse when a request arrives: 
```python3
from django.urls import path
from . import views #form current directory import views.py

urlpatterns = [
    path("", views.index, name="index")
]
"""
"": means the root path to the app localhost:800/hello/
views.index: function to execute when fetching root
name: way to use this url
"""

```

5. add the urls of the api to the main project's  `urls.py` 
```python3
"""hello_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include("hello.urls")) #include all urls from hello app "hello/urls.py"
]

```



