from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import re
import random

from . import util, helper, wiki_forms
from markdown2 import markdown


def index(request):

    entries_list =[]
    for name in util.list_entries():
        entries_list.append({'title': re.sub(r'_', ' ', name), 'url': name})

    return render(request, "encyclopedia/index.html", {
        "entries": entries_list
    })


def display_entry(request, title):


    correct_title, content = helper.get_entry(title, util.get_entry)
    entry_title_dict = {'title': re.sub(r'_', ' ', correct_title),
                        'url': correct_title}
    context = {'entry_title': entry_title_dict}

    if content == None:
        context['error_message'] = f"Page \"wiki/{title}\" Not found"
        return render(request, "encyclopedia/entry.html", context)

    #converting markdown to html
    context['entry_body'] = markdown(content)

    # to display the title as the same in the url
    if title != correct_title:
        # return HttpResponseRedirect(f"/wiki/{correct_title}")
        return HttpResponseRedirect(reverse("display_entry", args=(correct_title,)))

    return render(request, "encyclopedia/entry.html", context)





def search(request):
    if request.method == 'GET':
        if 'q' in request.GET:
            search_title = request.GET['q']

            # searching for a matching title
            search_title_seprated_with_underscore=re.sub(r'\s', '_', search_title)
            valid_title = helper.is_title_exists(search_title_seprated_with_underscore, util.list_entries())
            if valid_title:
                # redirect to the page requested
                # return HttpResponseRedirect(f"/wiki/{valid_title}")
                return HttpResponseRedirect(reverse("display_entry",
                                                    args=(valid_title,)))

            # trying to find mataches in the title
            search_matches_list=[]
            for title in util.list_entries():

                title_sperated_with_space = re.sub(r'_', ' ', title)
                if helper.in_title(search_title, title_sperated_with_space):
                    d = {'title': re.sub('_', ' ', title),
                         'title_url': title}
                    search_matches_list.append(d)

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

                # replace space with single underscore '_' ex: "ALLAH is one" to
                # "ALLAH_is_one"
                saved_title = re.sub(r"\s", '_', title)

                if helper.is_title_exists(saved_title, util.list_entries()):
                    # display error
                    context = {'title_exists_error': f"The title exists before Please Enter a different one, or go to the topic and edit it !",
                               'form': form}

                    return render(request, "encyclopedia/new_page.html", context)

                # if the tile is new (not exist)
                else:
                    # save entry
                    util.save_entry(saved_title, content)

                    # return HttpResponseRedirect(f"/wiki/{saved_title}")
                    return HttpResponseRedirect(reverse("display_entry",
                                                       args=(saved_title, )))

            else:
                context= {'form':form,
                          'content_not_filled_error': 'Please fill in the body of the topic'}
                return render(request, "encyclopedia/new_page.html", context)

    # for GET request
    context= {'form':wiki_forms.NewPage(initial=initial_data)}
    return render(request, "encyclopedia/new_page.html", context)





def edit_entry(request, title):


    correct_title, content = helper.get_entry(title, util.get_entry)
    entry_title_dict = {'title': re.sub(r'_', ' ', correct_title),
                        'url': correct_title}
    context = {'entry_title': entry_title_dict}

    if content == None:
        context['error_message'] = f"Page \"wiki/{title}\" Not found"
        return render(request, "encyclopedia/edit_entry.html", context)

    # to display the title as the same in the url
    if title != correct_title:
        # return HttpResponseRedirect(f"/wiki/edit/{correct_title}")
        return HttpResponseRedirect(reverse("edit_entry",
                                            args=(correct_title, )))


    initial_data = {'content': content}

    # submitting edit form
    if request.method == 'POST':
        form = wiki_forms.EditEntry(request.POST, initial=initial_data)
        if form.is_valid():
            content = form.cleaned_data['content']
            util.save_entry(entry_title_dict['url'], content)

            # return HttpResponseRedirect(f"/wiki/{entry_title_dict['url']}")
            return HttpResponseRedirect(reverse("display_entry",
                                               args=(entry_title_dict['url'], )))



    form = wiki_forms.EditEntry(initial = initial_data)
    context['form']=form

    return render(request, "encyclopedia/edit_entry.html", context)


def random_entry(request):
    entries_list = util.list_entries()
    random_entry = entries_list[random.randint(0, len(entries_list)-1)]

    # return HttpResponseRedirect(f"/wiki/{random_entry}")
    return HttpResponseRedirect(reverse("display_entry",
                                        args=(random_entry, )))


