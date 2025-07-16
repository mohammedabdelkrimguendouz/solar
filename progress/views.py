from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Progress
from .serializers import ProgressSerializer
from permission.permission import IsLeader
from users.models import User
from django.test import RequestFactory
from projects.models import Project
from rest_framework.test import force_authenticate
from notifications.views import SendNotificationAPIView

class ProgressCreateView(CreateAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
    permission_classes = [IsAuthenticated,IsLeader]

    def perform_create(self, serializer):
        serializer.save()
        admins = User.objects.filter(user_type='admin')

        if admins.exists():

            project = Project.objects.get(id=serializer.data['project'])
            message = f"New progress report for project : {project.name} has been updated by {self.request.user.username}"
            for admin in admins:
                request = RequestFactory().post(
                    '/',
                    data={
                        'user_id': admin.id,
                        'message': message
                    },
                    content_type='application/json'
                )
                force_authenticate(request, user=admin)


                response = SendNotificationAPIView.as_view()(request)



