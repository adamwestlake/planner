from django.urls import path
from . import views

# URL CONF
urlpatterns = [
    path('home/', views.main, name='home'),
    path('new/', views.new, name = 'new'),
    path('test/', views.delete_user, name='test'),
]