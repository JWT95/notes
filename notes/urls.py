from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.index, name='index'),
    path('like/<int:note_id>/', views.like, name='like'),
    path('post', views.post, name='post'),
]
