from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.submissions, name='post'),
    path('events/', views.events, name='events'),

    path('submission/<str:pk>/', views.submission, name='submission'),
    path('event/<str:pk>/', views.event, name='event'),

    path('create-submission/', views.createSubmission, name='create-submission'),
    path('update-submission/<str:pk>/', views.updateSubmission, name='update-submission'),
    path('delete-submission/<str:pk>/', views.deleteSubmission, name='delete-submission'),

    path('create-event/', views.createEvent, name='create-event'),
    path('update-event/<str:pk>/', views.updateEvent, name='update-event'),
    path('delete-event/<str:pk>/', views.deleteEvent, name='delete-event'),
]