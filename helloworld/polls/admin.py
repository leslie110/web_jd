from django.contrib import admin
from polls import models

# Register your models here.
class ControlUser(admin.ModelAdmin):
    '''自定义列表中栏目 添加list_display 属性'''
    list_display = ('user_name','psw','mail')
    search_fields = ('user_name',)

class ControlArticle(admin.ModelAdmin):
    '''自定义列表中栏目 添加list_display 属性'''
    list_display = ('id','title','auth','create_time','update_time')
    search_fields = ('title',)



admin.site.register(models.User,ControlUser)
admin.site.register(models.Person)
admin.site.register(models.Article,ControlArticle)
admin.site.site_header = 'XX项目后台系统'
admin.site.site_title = '登录系统后台'
admin.site.index_title = '后台管理'