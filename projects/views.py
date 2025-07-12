from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from permission.permission import IsAdmin, IsLeader
from django.db.models import Count, Sum, Avg
from users.models import User
from projects.models import Project
from progress.models import Progress
from rest_framework.generics import ListAPIView

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    
    def create(self, request, *args, **kwargs):
        print("Incoming data:", request.data) 
        return super().create(request, *args, **kwargs)



class GetProjectsByUserView(ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsLeader]
    def get_queryset(self):
        return Project.objects.filter(leader=self.request.user).order_by('-created_at')
        
class DashboardStatsView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        total_projects = Project.objects.count()
        completed_projects = Project.objects.filter(status=True).count()
        inCompleted_projects = Project.objects.filter(status=False).count()

        total_leaders = User.objects.filter(user_type='leader').count()
        total_panels_configured = Project.objects.aggregate(total=Sum('number_of_panels'))['total'] or 0

        total_panels_installed = Progress.objects.aggregate(total=Sum('panels_installed'))['total'] or 0
        avg_panels_per_project = Progress.objects.values('project') \
            .annotate(total_installed=Sum('panels_installed')) \
            .aggregate(avg=Avg('total_installed'))['avg'] or 0

        projects_per_leader = (
            Project.objects
            .values('leader__username')
            .annotate(project_count=Count('id'))
        )

        return Response({
            "total_projects": total_projects,
            "completed_projects": completed_projects,
            "inCompleted_projects": inCompleted_projects,
            "total_leaders": total_leaders,
            "total_panels_configured": total_panels_configured,
            "total_panels_installed": total_panels_installed,
            "avg_panels_per_project": round(avg_panels_per_project, 2),
            "projects_per_leader": projects_per_leader,
        })







