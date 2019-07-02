from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='member-list'),
    path('add', views.form, name='member-form'),
    path('', views.store, name='member-store'),
    path('', views.search, name='member-search')
]