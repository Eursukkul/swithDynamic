from django.db import models
from rest_framework import serializers
from rest_framework import generics

class TodoList(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    compiled = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
            model = TodoList
            fields = ('id', 'title', 'description', 'compiled')

class TodoListUpdateSerializer(serializers.ModelSerializer):
     class Meta:
                 model = TodoList
                 fields = ('id', 'title', 'description', 'compiled')

"""create a new TodoList"""
class TodoListCreateSerializer(generics.ListAPIView):
     quertset = TodoList.objects.all()
     serializer_class = TodoListUpdateSerializer

"""Update a TodoList"""
class TodoLisUpdaSerializer(generics.UpdateAPIView):
      queryset = TodoList.objects.all()
      serializer_class = TodoListUpdateSerializer

"""Delete a TodoList"""
class TodoListDeleteSerializer(generics.DestroyAPIView):
      queryset = TodoList.objects.all()
      serializer_class = TodoListUpdateSerializer

urlpatterns = [
      __path__('todo/',
               TodoListCreateSerializer.as_view(),
               name='todo-list-create'),
      __path__('todo/<int:pk>/',
               TodoLisUpdaSerializer.as_view(),
               name='todo-list-updte'),
      __path__('todo/<int:pk>/',
               TodoListDeleteSerializer.as_view(),
               name='todo-list-delete'),
]