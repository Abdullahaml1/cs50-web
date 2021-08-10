import re

"""
Trying all string patterns:(upper, lower, capitalize) to finding the matching title
Input:
     title: string
     func : func(string) and return None or string
Output:
     tuple (title, content)
"""
def get_entry(title, func):


    correct_title= title
    content = func(title)

    if content == None:
        # capitalize
        str_list = title.split('_')
        correct_title = '_'.join([str.lower().capitalize() for str in str_list])
        content = func(correct_title)
    else:
        return (correct_title, content)

    if content == None:
        # lower cases
        correct_title = title.upper()
        content = func(correct_title)
    else:
        return (correct_title, content)


    if content == None:
        # upper cases
        correct_title = title.lower()
        content = func(correct_title)

    return (correct_title, content)





"""
case insensitive string equality
"""
def is_title(title, correct_title):
    return title.lower() == correct_title.lower()



"""
case insensitive string matching
"""
def in_title(title, correct_title):
    return title.lower() in correct_title.lower()


