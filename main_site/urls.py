from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('photography/', views.photo_tags, name='photo'),
    path('photography/<int:tag_id>/', views.photo, name='photo'),
    path('writing/', views.writing, name='writing')
]
