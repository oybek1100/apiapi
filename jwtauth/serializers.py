from .models import Course , Module
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.db.models import Prefetch


from rest_framework import serializers

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'title']

class CourseSerializer(serializers.ModelSerializer):
    modules = serializers.SerializerMethodField()  
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_modules(self, obj):
        modules = obj.modules.all()[:100] 
        return ModuleSerializer(modules, many=True).data

    def get_owner(self, obj):
        return obj.owner.username


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



    