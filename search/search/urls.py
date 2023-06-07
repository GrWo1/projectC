from django.urls import path
from search_app.views import index, search_view

urlpatterns = [
    path('', index, name='index'),
    path('search_view/', search_view, name='search_view'),
]
