from django.urls import path , include
from .views import CourseViewset , SubjectViewset 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('course' , CourseViewset , basename='course')
router.register('subject' , SubjectViewset , basename='subject')

urlpatterns = [
    path('' , include(router.urls)),
]