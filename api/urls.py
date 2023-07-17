from django.urls import path
from .views import React, ListTodo


urlpatterns = [

    path('', React.as_view()),
    path('api/', ListTodo.as_view()),

]