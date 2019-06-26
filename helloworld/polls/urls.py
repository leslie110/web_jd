from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    url("^demo$",views.demo,name='demo'),
    url('^demo/page=(\d+)$',views.page),
    path("archive/<year>/<month>.html",views.home2),
    url(r"^archive1/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2}).html$",views.home1),
    url("^home",views.home),
    url("^leslie",views.leslie),
    url("^sonpage",views.sonpage),
    url('^qq/',views.test_qq),
    url('^result', views.result_qq),
    url('^select_mail/', views.select_mail),
    url('^logon/', views.register),
    url('^login/', views.log_in),
    url('^s_mail/', views.s_mail),
    url('^s_mass_mail/', views.s_mass_mail),
    url('^reset_psw/', views.reset_psw),
]