from django import forms

class CreateNewTaskForm(forms.Form):
    title = forms.CharField(label="titulo de tarea", max_length=200)
    description = forms.CharField(label ="descripcion de la tarea" ,widget=forms.Textarea)