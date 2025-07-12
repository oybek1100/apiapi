from django.urls import path , include
from .views import CourseViewset , ModuleViewset , CourseModuleAPIView
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView , SpectacularSwaggerView , SpectacularRedocView

router = DefaultRouter()
router.register('course' , CourseViewset , basename='course')
router.register('module' , ModuleViewset , basename='module')

urlpatterns = [
    path('' , include(router.urls)),
    path('course/<int:pk>/modules' , CourseModuleAPIView.as_view() , name='course-module'),
    path('schema/' , SpectacularAPIView.as_view() , name='schema'),
    path('schema/swagger/' , SpectacularSwaggerView.as_view(url_name='schema') , name='swagger-ui'),
    path('schema/redoc/' , SpectacularRedocView.as_view(url_name='schema') , name='redoc'),
]