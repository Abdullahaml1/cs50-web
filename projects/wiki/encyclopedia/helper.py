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
        correct_title = title.lower().capitalize()
        content = func(correct_title)
    else:
        return (correct_title, content)

    if content == None:
        correct_title = title.upper()
        content = func(correct_title)
    else:
        return (correct_title, content)


    if content == None:
        correct_title = title.lower()
        content = func(correct_title)

    return (correct_title, content)






def is_title(title, correct_title):

    def func(x, y):
        return x == y

    return pattern_search(title, correct_title, func)


def in_title(title, correct_title):
    def func(x, y):
        return x in y

    return pattern_search(title, correct_title, func)



"""
Trying all string patterns:(upper, lower, capitalize) to finding the matching title
Input:
     title: string
     correct_title : string to compared
     func: function that returns true and false
Output:
   returns True: if the title is found in the patterns
           Fales if failed in all patterns
"""
def pattern_search(title, correct_title, func):

    if func(title, correct_title):
        return True


    if func(title.lower().capitalize(), correct_title):
        return True

    if func(title.lower(), correct_title):
        return True

    if func(title.upper(), correct_title):
        return True

    return False
