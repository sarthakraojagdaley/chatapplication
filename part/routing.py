from . import consumers
from django.urls import path
webscoket_urlpatterns=[
    path("ws/ac/",consumers.AsyncConsumer.MySync_Consumer.as_asgi())
]