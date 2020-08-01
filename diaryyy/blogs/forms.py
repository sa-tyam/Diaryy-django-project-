#blogs forms.py

from django import forms
from . import models

class BlogForm(forms.ModelForm):
    class Meta:
        fields = ('blog_image', 'message')
        model = models.Blog

    def __init__(self, *args, **kwrags):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
