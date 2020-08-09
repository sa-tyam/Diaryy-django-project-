# blogs views.py

from django.shortcuts import render, get_object_or_404, redirect
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.views import generic
from braces.views import SelectRelatedMixin
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth import get_user_model
User = get_user_model()

class BlogList(SelectRelatedMixin, generic.ListView):
    model = models.Blog
    select_related = ('user',)

class RandomBlogList (generic.ListView):
    model = models.Blog
    template_name = 'blogs/user_random_blog.html'

    def get_queryset(self):
        try:
            self.blog_user = User.objects.prefetch_related('blogs').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.blog_user.blogs.order_by('?')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_user'] = self.blog_user
        return context



class UserBlog(generic.ListView):
    model = models.Blog
    template_name='blogs/user_blog_list.html'

    def get_queryset(self):
        try:
            self.blog_user = User.objects.prefetch_related('blogs').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.blog_user.blogs.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_user'] = self.blog_user
        return context

class BlogDetailView(SelectRelatedMixin, generic.DetailView):
    model = models.Blog
    select_related= ('user',)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )

class BlogCreateView(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView ):
    fields = ('blog_image', 'message')
    model = models.Blog

    def  form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)

class BlogDeleteView(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    select_related = ('user',)
    model = models.Blog
    success_url = reverse_lazy('blogs:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Blog deleted")
        return super().delete(*args, **kwargs)
