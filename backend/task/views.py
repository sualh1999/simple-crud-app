from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer


class TaskListCreateView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return None

    def put(self, request, pk):
        task = self.get_object(pk)
        if not task:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        # Toggle task completion
        task.is_complete = not task.is_complete
        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def delete(self, request, pk):
        task = self.get_object(pk)
        if not task:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
