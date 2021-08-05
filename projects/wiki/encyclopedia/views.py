from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import util, helper, wiki_forms
from markdown2 import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def display_entry(request, title):


    correct_title, content = helper.get_entry(title, util.get_entry)
    context = {'entry_title': correct_title}

    if content == None:
        context['error_message'] = f"Page \"wiki/{title}\" Not found"
        return render(request, "encyclopedia/entry.html", context)

    #converting markdown to html
    context['entry_body'] = markdown(content)

    # to display the title as the same in the url
    if title != correct_title:
        return HttpResponseRedirect(f"/wiki/{correct_title}")

    return render(request, "encyclopedia/entry.html", context)





def search(request):
    if request.method == 'GET':
        if 'q' in request.GET:
            search_title = request.GET['q']

            # searching for the titles
            for title in util.list_entries() :

                if helper.is_title(search_title, title):

                    # redirect to the page requested
                    return HttpResponseRedirect(f"/wiki/{title}")

            # trying to find mataches in the title
            search_matches_list=[]
            for title in util.list_entries():

                if helper.in_title(search_title, title):
                    search_matches_list.append(title)

            context = {'search_title': search_title}
            if search_matches_list == []:
                context['error_message']=f"No search result for \"{search_title}\""

            else:
                context['search_matches_list'] = search_matches_list

            return render(request, "encyclopedia/search.html", context)



def new_page(request):

    initial_data = {'content': "Type HERE the body of the topic"}

    if request.method == "POST":
        form = wiki_forms.NewPage(request.POST, initial=initial_data)

        if form.is_valid():

            # checking that all fields values has changed
            if len(form.changed_data) == len(form.cleaned_data):

                title = form.cleaned_data['title']
                content = form.cleaned_data['content']

                # TODO ------------------------------------->>>>>>>>>>>>>>>>>
                saved_title = '-'.join(title.split(' '))
                util.save_entry(title, content)

                return HttpResponseRedirect(f"/wiki/{title}")

            else:
                context= {'form':form}
                return render(request, "encyclopedia/new_page.html", context)

    # for GET request
    context= {'form':wiki_forms.NewPage(initial=initial_data)}
    return render(request, "encyclopedia/new_page.html", context)
