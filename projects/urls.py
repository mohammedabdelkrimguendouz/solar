from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet
from django.urls import path, include
from .views import GetProjectsByUserView , DashboardStatsView


router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get-projects-by-user/', GetProjectsByUserView.as_view(), name='get-projects-by-user'),
    path('dashboard-statistics/', DashboardStatsView.as_view(), name='dashboard-statistics'),
]
