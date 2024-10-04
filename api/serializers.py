from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from employee.models import User, Team, Position, Skill, Competence, Rating, LastDateMatch


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = '__all__'


class CompetenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competence
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    competence = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Skill
        fields = 'name', 'domain', 'competence'


class LastDateSerializer(serializers.ModelSerializer):
#    last_date_match = serializers.CharField(source="LastDateSerializer.match")
    
    class Meta:
        model = LastDateMatch
#        fields = 'last_date_match', 'date_last_score'
        fields = 'match', 'date_last_score'

class RaitingSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(read_only=True)
    last_date = LastDateSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = (
            'skill', 'score', 'date_score', 'need_to_study',
            'date', 'date_start', 'date_end', 'match', 'chief_proof', 'last_date',
        )


class UserSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField(read_only=True)
    rating = RaitingSerializer(many=True, read_only=True)
    

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'date_hire', 'date_fire',
            'position', 'grade', 'role', 'key_people', 'bus_factor', 'emi',
            'rating',
        )

