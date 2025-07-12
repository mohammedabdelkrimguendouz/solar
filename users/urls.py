from django.urls import path
from .views import LoginView
from .views import RegisterView
from .views import LeaderUsersView
from .views import ChangePasswordView
from .views import UserProfileView
from .views import TokenRefreshView
from .views import LeaderDeleteView
from .views import ToggleLeaderStatus

urlpatterns = [
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('leader-users/', LeaderUsersView.as_view(), name='leader-users'),
    path('leader-users/<int:pk>/', LeaderDeleteView.as_view(), name='leader-delete'),
    path('leader-users/<int:pk>/toggle_active/', ToggleLeaderStatus.as_view(), name='leader-toggle'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('me/', UserProfileView.as_view(), name='user_profile'),
]
