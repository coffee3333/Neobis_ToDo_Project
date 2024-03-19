from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    # def get_queryset(self):
    #     # Only allow users to see their own todo items
    #     return Todo.objects.filter(user=self.request.user)

    # def perform_create(self, serializer):
    #     # Automatically associate the todo item with the logged-in user
    #     serializer.save(user=self.request.user)