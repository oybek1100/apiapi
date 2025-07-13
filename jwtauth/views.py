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
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache

class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all().select_related('owner')
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    @method_decorator(cache_page(60 * 15))
    def list(self, request, *args, **kwargs):
        print("DB QUERY")  # caching ishlayaptimi tekshirish uchun
        return super().list(request, *args, **kwargs)


class ModuleViewset(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cache_key = "module_list"
        modules = cache.get(cache_key)

        if modules is None:
            modules = Module.objects.all()
            cache.set(cache_key, modules, timeout=60 * 15)

        return modules  

class CourseModuleAPIView(ListAPIView):
    serializer_class = ModuleSerializer

    def get_queryset(self):
        course_id = self.kwargs['pk']
        cache_key = f"course_{course_id}_modules"

        modules = cache.get(cache_key)
        if modules is None:
           
            modules = Module.objects.filter(course_id=course_id)
            cache.set(cache_key, modules, timeout=60 * 15)  # 15 daqiqa
      

        return modules

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