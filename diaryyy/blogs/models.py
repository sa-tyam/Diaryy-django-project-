# blogs models.py

from django.db import models
from django.urls import reverse
from django.conf import settings
import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

class Blog(models.Model):
    user = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    message = models.TextField(unique=False, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    message_html = models.TextField(editable=False)
    blog_image = models.ImageField(default='', upload_to='', blank=False, null=False )

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']
