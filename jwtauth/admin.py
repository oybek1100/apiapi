from django.contrib import admin
from .models import Course , Module

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title' , 'course')
    

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title' , 'owner', 'image')

admin.site.register(Course , CourseAdmin)
admin.site.register(Module , ModuleAdmin)

