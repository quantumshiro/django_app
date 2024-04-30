from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/tasks', views.index, name='tasks.index'),
    path('create', views.create_folder, name='folders.create'),
]