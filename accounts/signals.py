from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    '''Это функция приемника, которая запускается каждый раз при создании пользователя.
    Пользователь является отправителем, который несет ответственность за отправку уведомления.'''
    if created:
        Profile.objects.create(user=instance)

