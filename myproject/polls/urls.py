from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('add',views.add, name='add'),
    path('', views.home, name='home')
] 