
from progress.views import ProgressCreateView
from django.urls import path, include


urlpatterns = [
    path('add-progress/', ProgressCreateView.as_view(), name='add-progress'),
]
