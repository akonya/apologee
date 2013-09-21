from django.conf.urls import patterns, include, url
from apps.api import views

urlpatterns = patterns('',
    url('test$',views.test),
    url('signup$',views.signup),
    url('login$',views.login),
    url('sorry$',views.sorry),
    url('accepted$',views.accepted),
)
