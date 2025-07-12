from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Progress
from .serializers import ProgressSerializer
from permission.permission import IsLeader

class ProgressCreateView(CreateAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
    permission_classes = [IsAuthenticated,IsLeader]

    def perform_create(self, serializer):
        serializer.save()
