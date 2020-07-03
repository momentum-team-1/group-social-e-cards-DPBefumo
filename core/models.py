from django.db import models
from users.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models import Q

# Create your models here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

COLOR_CHOICES = {
    ('Ash Gray', 'Ash Gray'),
    ('Gunmetal', 'Gunmetal'),
    ('Baby Powder', 'Baby Powder'),
    ('Indigo Dye', 'Indigo Dye'),
    ('Ivory', 'Ivory'),
}

BORDER_CHOICES = {
    ('', ''),
    ('', ''),
    ('', ''),
    ('', ''),
    ('', ''),
}

FONT_CHOICES = {
    ('', ''),
    ('', ''),
    ('', ''),
    ('', ''),
    ('', ''),
}

class Card(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='cards', null=True)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    inner_message = models.CharField(max_length=255, null=True, blank=True)
    outer_message = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=100, choices=COLOR_CHOICES, default='Baby Powder')
    border = models.CharField(max_length=100, choices=BORDER_CHOICES, default='')
    font = models.CharField(max_length=100, choices=FONT_CHOICES, default='')



