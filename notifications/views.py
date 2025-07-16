
from django.http import JsonResponse
from notifications.models import Notification
from channels.layers import get_channel_layer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, ValidationError
from notifications.models import Notification
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from users.models import User
from .serializers import NotificationSerializer
from permission.permission import IsAdmin


class GetNotificationsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            notifications = Notification.objects.filter(
                recipient=request.user
            ).order_by('-created_at')
            
            serializer = NotificationSerializer(notifications, many=True)
            
            return Response({"notifications": serializer.data}, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)





class SendNotificationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user_id = request.data.get('user_id')
            message = request.data.get('message')
            
            if not user_id or not message:
                raise ValidationError("user_id and message are required")
            
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                raise NotFound("User not found")
            
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
            
            return Response({
NotificationSerializer(notification).data
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)



class MarkAsReadAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, notification_id):
        try:
            notification = Notification.objects.get(id=notification_id)
            notification.is_read = True
            notification.save()
            
            return Response({
                "status": "success",
                "message": "Notification marked as read"
            }, status=status.HTTP_200_OK)
            
        except Notification.DoesNotExist:
            raise NotFound("Notification not found")
        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)



