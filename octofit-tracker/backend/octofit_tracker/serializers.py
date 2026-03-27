
from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard
from bson import ObjectId

class ObjectIdFieldSerializer(serializers.Field):
    def to_representation(self, value):
        return str(value) if value else None
    def to_internal_value(self, data):
        return ObjectId(data) if data else None


class TeamSerializer(serializers.ModelSerializer):
    id = ObjectIdFieldSerializer(read_only=True)
    class Meta:
        model = Team
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    id = ObjectIdFieldSerializer(read_only=True)
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), source='team', write_only=True, required=False)
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'team', 'team_id']


class ActivitySerializer(serializers.ModelSerializer):
    id = ObjectIdFieldSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_id', 'activity_type', 'duration', 'date']


class WorkoutSerializer(serializers.ModelSerializer):
    id = ObjectIdFieldSerializer(read_only=True)
    suggested_for = UserSerializer(many=True, read_only=True)
    suggested_for_ids = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='suggested_for', many=True, write_only=True, required=False)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'suggested_for', 'suggested_for_ids']


class LeaderboardSerializer(serializers.ModelSerializer):
    id = ObjectIdFieldSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'user_id', 'score', 'rank']
