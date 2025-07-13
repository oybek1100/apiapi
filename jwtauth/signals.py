from django.db.models.signals import post_delete , post_save
from django.core.cache import cache
from django.dispatch import receiver
from .models import Course , Module


@receiver([post_delete , post_save] , sender=Course)
def update_cache(sender , instance , **kwargs):
    cache_key = 'course_list'
    cache.delete(cache_key)

    courses = Course.objects.all()
    cache.set(cache_key , courses , timeout=60 * 15)

@receiver([post_delete , post_save] , sender=Module)
def update_cache(sender , instance , **kwargs):
    cache_key = 'module_list'
    cache.delete(cache_key)

    modules = Module.objects.all()
    cache.set(cache_key , modules , timeout=60 * 15)