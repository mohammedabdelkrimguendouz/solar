from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model
from rest_framework.exceptions import NotFound
from .models import Notification
from .serializers import NotificationSerializer
from users.models import User



def send_notification_to_user(user_id, message):
    try:
        user = User.objects.get(id=user_id)
    except Exception as e:
        raise NotFound(f"User not found: {e}")


    notification = Notification.objects.create(
        recipient=user,
        message=message
    )


    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"notifications_{user.id}",
        {
            "type": "send.notification",
            "notification": NotificationSerializer(notification).data
        }
    )

    return notification

