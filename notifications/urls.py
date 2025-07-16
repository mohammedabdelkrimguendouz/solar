from django.urls import path
from .views import SendNotificationAPIView, GetNotificationsAPIView ,MarkAsReadAPIView

urlpatterns = [
    path('send-notification/', SendNotificationAPIView.as_view(), name='send_notification'),
    path('get-notifications/', GetNotificationsAPIView.as_view(), name='get_notifications'),
    path('mark-as-read/<int:notification_id>/', MarkAsReadAPIView.as_view(), name='mark_as_read'),

]
