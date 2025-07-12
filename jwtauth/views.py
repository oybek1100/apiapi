from django.shortcuts import render
from .models import Course , Module
from .serializers import CourseSerializer , ModuleSerializer ,CustomTokenObtainPairSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all().select_related('owner')
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    


class ModuleViewset(viewsets.ModelViewSet):
    queryset = Module.objects.all() 
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]  

class CourseModuleAPIView(ListAPIView):
    serializer_class = ModuleSerializer
    
    def get_queryset(self):
        cours_id = self.kwargs['pk']
        return Module.objects.filter(course_id=cours_id)
        



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"detail": "Invalid refresh token."}, status=status.HTTP_400_BAD_REQUEST)