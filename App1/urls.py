


from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('callback/', views.callback_view, name='callback_view'),
    path('callback_listener/', views.callback_listener_view, name='callback_listener'),
]



