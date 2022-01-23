from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('photography/', views.photo, name='photo'),
    path('writing/', views.writing, name='writing'),
    path('<slug:slug>/', views.photo, name='photo')
]
