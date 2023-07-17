from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from django.views.generic import TemplateView


class React(TemplateView):
    template_name = 'index.html'

class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

