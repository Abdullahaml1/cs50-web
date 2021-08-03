from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import util
from . import helper
from markdown2 import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def display_entry(request, title):


    correct_title, content = helper.get_entry(title, util.get_entry)
    context = {'entry_title': correct_title}

    if content == None:
        context['error_message'] = "Page Not found"
        return render(request, "encyclopedia/entry.html", context)

    #converting markdown to html
    context['entry_body'] = markdown(content)

    # to display the title as the same in the url
    if title != correct_title:
        return HttpResponseRedirect(f"/wiki/{correct_title}")

    return render(request, "encyclopedia/entry.html", context)
