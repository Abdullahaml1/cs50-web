from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import datetime

# Create your views here.


def index(request):
    now = datetime.datetime.now()
    template = loader.get_template("newyear/index.html")
    context = {"is_new_year": now.year==2022 and now.month==1}
    return HttpResponse(template.render(context, request))
# short way for rendering the template
# def index(request):
#     return render(request, "newyear/index.html", {"is_new_year": False})
