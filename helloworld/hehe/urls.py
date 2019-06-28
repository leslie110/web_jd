from django.conf.urls import url
from hehe import views

urlpatterns = [
    url('^login/$',views.hehe_login),
    url('^logon/$', views.hehe_logon),
    url('^reset_psw/$', views.hehe_reset_psw),
]