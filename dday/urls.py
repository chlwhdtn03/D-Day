from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('addEvent/', views.addEvent, name='addEvent'),
    path('addComment/', views.addComment, name='addComment'),
    path('deleteEvent/', views.deleteEvent, name='deleteEvent'),
]
app_name = 'dday'