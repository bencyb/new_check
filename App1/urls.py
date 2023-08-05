
from django.urls import path
from .views import webhook_callback
# ,create_webhook

urlpatterns = [
    path('webhook/', webhook_callback, name='webhook-callback'),
    # path('create_webhook/', create_webhook, name='create_webhook'),
]
