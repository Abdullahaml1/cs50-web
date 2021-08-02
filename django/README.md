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

# Cross-site resource forgery (csrf)
We need to add a bit more to this form now, because Django requires a token to prevent Cross-Site Request Forgery (CSRF) Attack. This is an attack where a malicious user attempts to send a request to your server from somewhere other than your site. This could be a really big problem for some websites. Say, for example, that a banking website has a form for one user to transfer money to another one. It would be catastrophic if someone could submit a transfer from outside of the bank’s website!

To solve this problem, when Django sends a response rendering a template, it also provides a CSRF token that is unique with each new session on the site. Then, when a request is submitted, Django checks to make sure the CSRF token associated with the request matches one that it has recently provided. Therefore, if a malicious user on another site attempted to submit a request, they would be blocked due to an invalid CSRF token. This CSRF validation is built into the Django Middleware framework, which can intervene in the request-response processing of a Django app. We won’t go into any more detail about Middleware in this course, but do look at the documentation if interested!

To incorporate this technology into our code, we must add a line to our form in add.html.
```html
<form action="{% url 'tasks:add' %}" method="post">
    {% csrf_token %}
    <input type="text", name="task">
    <input type="submit">
</form>


```
This line adds a hidden input field with the CSRF token provided by Django, such that when we reload the page, it looks as though nothing has changed. However, if we inspect element, we’ll notice that a new input field has been added: 
```html
<input type="hidden" name="csrfmiddlewaretoken" value="XLP5CtxjjXSvRSDrtPxbvfUrOtnpfPy3NiUR0HCpdt57j9MN54roy0bZztp9v596">
```

# Django Forms [taskform app](django_project/taskform)
* **Resources:** [django forms tutorial](https://docs.djangoproject.com/en/3.2/topics/forms/), [django filed reference](https://docs.djangoproject.com/en/3.2/ref/forms/fields/)

* django forms has a class `django.forms.Form` class that generate an boject that is fieled with the forms fields and generates a variable coressponds to the forms html
* also manipulates the form inputs and validations extra
## example: 
* create a file contains your forms let's call it `my_forms.py`
```python3
from django import forms

class TaskForm (forms.Form):
    taskname = forms.CharField(label="Task Name", max_length=100)

```

This defines a Form class with a single field (taskname). We’ve applied a human-friendly label to the field, which will appear in the <label> when it’s rendered (although in this case, the label we specified is actually the same one that would be generated automatically if we had omitted it).

The field’s maximum allowable length is defined by max_length. This does two things. It puts a maxlength="100" on the HTML <input> (so the browser should prevent the user from entering more than that number of characters in the first place). It also means that when Django receives the form back from the browser, it will validate the length of the data.

A Form instance has an is_valid() method, which runs validation routines for all its fields. When this method is called, if all fields contain valid data, it will:

    return True
    place the form’s data in its cleaned_data attribute.


* and our html page `add.html` will look like this:
```html
{% extends "taskform/layout.html" %}
{% block body %}
<h2> Add Task: </h2>
<form action="{% url 'taskform:add' %}" method="POST" >
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Sbumit" >
</form>
<a href="{% url 'taskform:index' %}" > My Tasks </a>
{% endblock %}

```
after rendering the form variable will be:
```html
<tr><th><label for="id_taskname">Task Name:</label></th><td><input type="text" name="taskname" maxlength="100" required id="id_taskname"></td></tr>

```


## Retrieving data from the form
Form data sent back to a Django website is processed by a view, generally the same view which published the form. This allows us to reuse some of the same logic.

To handle the form we need to instantiate it in the view for the URL where we want it to be published: views.py
```python3
def add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = myforms.TaskForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            task = form.cleaned_data["taskname"]
            # request.session['tasks_list'] += [task]
            request.session['tasks_list'].append(task)
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/taskform/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = myforms.TaskForm()

    context = {'form': form}
    return render(request, 'taskform/add.html', context)

```
If we arrive at this view with a GET request, it will create an empty form instance and place it in the template context to be rendered. This is what we can expect to happen the first time we visit the URL.

If the form is submitted using a POST request, the view will once again create a form instance and populate it with data from the request: form = TaskForm(request.POST) This is called “binding data to the form” (it is now a bound form).

We call the form’s is_valid() method; if it’s not True, we go back to the template with the form. This time the form is no longer empty (unbound) so the HTML form will be populated with the data previously submitted, where it can be edited and corrected as required.

If is_valid() is True, we’ll now be able to find all the validated form data in its cleaned_data attribute. We can use this data to update the database or do other processing before sending an HTTP redirect to the browser telling it where to go next.
* The template `add.html`
```html
{% extends "taskform/layout.html" %}
{% block body %}
<h2> Add Task: </h2>
<form action="{% url 'taskform:add' %}" method="POST" >
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Sbumit" >
</form>
<a href="{% url 'taskform:index' %}" > My Tasks </a>
{% endblock %}

```

# Sessions [code from taskform app](django_project/taksform)

At this point, we’ve successfully built an application that allows us to add tasks to a growing list. However, it may be a problem that we store these tasks as a global variable, as it means that all of the users who visit the page see the exact same list. In order to solve this problem we’re going to employ a tool known as sessions.

Sessions are a way to store unique data on the server side for each new visit to a website.
* from `views.py`
```python3
def add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = myforms.TaskForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            task = form.cleaned_data["taskname"]
            # request.session['tasks_list'] += [task]
            request.session['tasks_list'].append(task)
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/taskform/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = myforms.TaskForm()

    context = {'form': form}
    return render(request, 'taskform/add.html', context)

```
Finally, before Django will be able to store this data, we must run `python manage.py migrate` in the terminal. Next week we’ll talk more about what a migration is, but for now just know that the above command allows us to store sessions.
