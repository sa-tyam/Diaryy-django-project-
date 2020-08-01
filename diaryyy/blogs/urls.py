# blogs urls.py

from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.BlogList.as_view(), name='all'),
    path('new/', views.BlogCreateView.as_view(), name='new'),
    url(r"by/(?P<username>[-\w]+)/$",views.UserBlog.as_view(),name="for_user"),
    url(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.BlogDetailView.as_view(),name="single"),
    url(r"delete/(?P<pk>\d+)/$",views.BlogDeleteView.as_view(),name="delete"),
]
