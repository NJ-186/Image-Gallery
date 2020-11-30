from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('search',views.search,name='search'),
    path('add',views.add,name='add'),   
    path('img/<int:pk>',views.image,name='image')
]