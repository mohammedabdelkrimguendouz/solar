from rest_framework import serializers
from .models import Project
from users.serializers import UserSerializer
from progress.serializers import ProgressSerializer
from users.models import User

class ProjectSerializer(serializers.ModelSerializer):
    leader = UserSerializer(read_only=True)
    progress = ProgressSerializer(many=True, read_only=True)
    leader_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='leader',
        write_only=True
    )
    
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 
                'number_of_panels', 'status', 'leader', 'leader_id', 'progress')
        extra_kwargs = {
            'progress': {'required': False},
        }

    def create(self, validated_data):
        leader = validated_data.pop('leader')
        project = Project.objects.create(leader=leader, **validated_data)
        return project
