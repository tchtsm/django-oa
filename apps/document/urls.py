from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='document'),
    path('/pdf', views.pdf, name='document-pdf'),
    path('add', views.form, name='member-form'),
    path('', views.store, name='member-store'),
    path('', views.search, name='member-search')
]