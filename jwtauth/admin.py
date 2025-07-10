from django.contrib import admin
from .models import Course , Subject

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title' , 'slug' , 'image')
    prepopulated_fields = {'slug':('title',)}

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title' , 'owner',   'subject' ,'image')

admin.site.register(Course , CourseAdmin)
admin.site.register(Subject , SubjectAdmin)
# Register your models here.
