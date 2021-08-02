from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import myforms

# Create your views here.



def index(request):

    # Check if there already exists a "tasks" key in our session
    if "tasks_list" not in request.session:

        # If not, create a new list
        request.session["tasks_list"] = []

    context = {'tasks_list': request.session['tasks_list']}
    return render(request, "taskform/index.html", context)



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
