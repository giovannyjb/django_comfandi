from statistics import mode
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404

from . import models, forms

# Create your views here.

def hello (request, username):
    return HttpResponse("<h1>Hello Gio %s</h1>"% username)


def projects(request):
    projects = list(models.Project.objects.values())
    return JsonResponse(projects,safe=False)

def projects_view(request):
    projects = models.Project.objects.all()
    return render(request, 'projects.html',{'projects':projects})

def tasks(request,id):
    task = get_object_or_404(models.Task,id=id)
    return HttpResponse('task: %s'% task.t)

def create_task(request):

    if  request.method == 'GET':
        return render(request , 'create_task.html',
        {
            'form':forms.CreateNewTaskForm
        })
    else:
        models.Task.objects.create(title = request.POST['title'], description = request.POST['description'],project_id=1)

        return redirect('/gio/projects')


def home(request):
    name = "Giovanni La maravilla"
    return render(request, 'index.html',{'name':name})