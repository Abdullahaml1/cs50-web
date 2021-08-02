from django import forms

class TaskForm (forms.Form):
    taskname = forms.CharField(label="Task Name", max_length=100)
    priority = forms.IntegerField(label="Priority", required=False,
                            min_value=0, max_value=10)
