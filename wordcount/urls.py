from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name='homepage'),
    path('countword', views.submits, name = 'submits')
]
