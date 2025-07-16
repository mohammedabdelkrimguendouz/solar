from rest_framework import serializers
from .models import Project
from users.serializers import UserSerializer
from progress.serializers import ProgressSerializer
from users.models import User

class ProjectSerializer(serializers.ModelSerializer):
    leader = UserSerializer(read_only=True)
    progress = ProgressSerializer(many=True, read_only=True)
    leader_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 
                'number_of_panels', 'status', 'leader', 'leader_id', 'progress')
        extra_kwargs = {
            'progress': {'required': False},
        }

    def create(self, validated_data):
        leader_id = validated_data.pop('leader_id')
        leader = User.objects.get(id=leader_id)
        project = Project.objects.create(leader=leader, **validated_data)
        return project
