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

class ControlBank(admin.ModelAdmin):
    '''自定义列表中栏目 添加list_display 属性'''
    list_display = ('bank_name','city','point')
    search_fields = ('bank_name',)

class ControlCardInfo(admin.ModelAdmin):
    '''自定义列表中栏目 添加list_display 属性'''
    list_display = ('card_id','card_name','info')
    search_fields = ('card_id',)



admin.site.register(models.User,ControlUser)
admin.site.register(models.Person)
admin.site.register(models.Article,ControlArticle)
admin.site.register(models.Bank,ControlBank)
admin.site.register(models.CardInfo,ControlCardInfo)
admin.site.site_header = 'XX项目后台系统'
admin.site.site_title = '登录系统后台'
admin.site.index_title = '后台管理'