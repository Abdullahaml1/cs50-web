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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include("hello.urls")) #include all urls from hello app "hello/urls.py"
]

```

6. run your project and test your `hello` app:
```
python3 manage.py runserver
```

7. open your browser and enter `localhost:8000/hello` your will see hello world

# Django Templates
A template is and html file to be viewed to the user
1. template should be in `<app name>/templates/<app name>/index.html` </br>
2. styles sheets and `static` files should be in `<app name>/static/<app name>/index.html` and to use it at the html document
```html

{% load static %} <!-- load static files -->
<!DOCTYPE html>
<html>
    <head>
        <title> New Year </title>
    </head>
    <link rel="stylesheet" href="{% static 'newyear/styles.css' %}">
    <body> 

        {% if is_new_year %}
        <h1> YES </h1>
        {% else %}
        <h1> NO </h1>
        {% endif %}

    </body>
</html>
```

3. then write the function to load this template in `views.py`
```python3
def index(request):
    now = datetime.datetime.now()
    template = loader.get_template("newyear/index.html")
    context = {"is_new_year": now.year==2022 and now.month==1}
    return HttpResponse(template.render(context, request))
# short way for rendering the template
# def index(request):
#     return render(request, "newyear/index.html", {"is_new_year": False})

```
That code loads the template called polls/index.html and passes it a context. The context is a dictionary mapping template variable names to Python objects.


# Layout and Template inheritance
to use a base template and include it into all html pages of the app or in all the project:
* in `<app name>/templates/<app name>/layout.html`
```html

<!DOCTYPE html>
<html lang="en">
    <head>
        <title> Tasks </title>
    </head>
    <body>
        <header>
            <a href="{% url 'tasks:index' %}">TODO</a>
            <a href="{% url 'tasks:add' %}">Add a New Task</a>
        </header>
        {% block body %} 
        {% endblock %}
    </body>
</html>
```
we defined a block called `body` we can name it any thing that we will use to insert our html code
* in `<app name>/templates/<app name>/index.html`
```html
{% extends "tasks/layout.html" %}

{% block body %}

<h2> TODO List </h1>
<ul>
    {% for task in tasks_list %}
    <li> {{ task }} </li>
    {% endfor %}
</ul>
{% endblock %}

```
`{% extends "tasks/layout.html" %}` means include this `layout.html`

## good way to add urls in the webpage
`<a href="{% url 'tasks:index' %}">TODO</a>` is to use `url` keyword of template language of django this will include `<app name>/urls` with its name like this
`path("", views.index, name="index")` and the actual url will be `tasks/index`
* **in order to use app name inside {% url %} we have to put a variable `app_name='<the app name>'` into ``urls.py``**
```python3
from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]
```


