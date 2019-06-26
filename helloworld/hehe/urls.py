from django.conf.urls import url
from hehe import views

urlpatterns = [
    url('^h_login/$',views.h_login),
]