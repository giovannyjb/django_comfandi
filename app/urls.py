
from django.urls import path
from . import views


urlpatterns = [
    path('hello/<str:username>', views.hello ),
    path('tasks/<int:id>', views.tasks ),
    path('projects/', views.projects ),
    path('home/',views.home)
]
