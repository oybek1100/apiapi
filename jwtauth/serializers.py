from .models import Course , Subject
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CourseSerializer(serializers.ModelSerializer):

    owner = serializers.SerializerMethodField()
    def get_owner(self , obj):
        return obj.owner.username
    class Meta:
        model = Course
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):

    courses = CourseSerializer(many=True , read_only=True)
    class Meta:
        model = Subject
        fields = '__all__'

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod

    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['id'] = user.id
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['id'] = self.user.id
        return data



    