from django.urls import path
from . import views

app_name = 'conversation'

urlpatterns = [
    path('new/<int:item_pk>',views.new_converastion,name='new'),
]