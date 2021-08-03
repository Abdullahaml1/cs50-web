

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


