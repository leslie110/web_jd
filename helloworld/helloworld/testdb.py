from django.http import HttpResponse,JsonResponse
from polls.models import Test,Person,User
from django.core import serializers
import json
from django.forms.models import model_to_dict

# 数据库操作
def testdb(request):
    test1 = Test(name='leslie1')
    test2 = Person(name='hehe01',age=20)
    test1.save()
    test2.save()
    return HttpResponse("数据库hello_test添加name成功！看去看看吧")

def add_user(request):
    test1 = User(user_name='呵呵哒',
                 psw='55555')
    test1.save()
    return HttpResponse("数据库polls_user添加name成功！看去看看吧")

def update_psw(request):
    test1 = User.objects.get(user_name='yoyo')
    test1.mial = '9999ppp'
    test1.save()
    return HttpResponse("数据库polls_user修改psw成功！看去看看吧")

def delete_user(request):
    test1 = User.objects.get(user_name='yoyo')
    test1.delete()
    return HttpResponse("数据库polls_user删除user成功！看去看看吧")

def select_user(request):
    # sql = connection.queries
    # objects.all()相当于sql语句的select * from User;
    a = User.objects.all()
    sql = a.query

    users = ''
    psws = ''
    mials = ''
    for i in a:
        users += ' '+i.user_name
        psws += ' '+i.psw
        mials += ' '+i.mial
    return HttpResponse('''<p>查询user结果：%s</p>
                        <p>查询psw结果：%s</p>
                        <p>查询psw结果：%s</p>
                        <p>sql:%s</p>''' % (users, psws, mials,sql))

def select_user1(request):
    # objects.filter(user_name='yoyo',
    #                psw=55555)
    # 相当于sql语句的select * from User where user_name='yoyo' and psw=55555
    b = User.objects.filter(user_name='yoyo',
                            psw=55555)
    sql = b.query
    try:
        result = b[0].user_name

    except Exception :
        result = 'null'
    return HttpResponse('<p>查询结果:%s</p><p>%s'%(result,sql))

def select_user2(request):
    # django的get是从数据库的取得唯一个匹配的结果，返回一个对象
    c = User.objects.get(user_name='yoyo').psw
    return HttpResponse('<p>查询结果:%s</p>'%c)


def select_user3(request):
    # all()和filter()返回的都是可迭代的queryset序列，平常我们习惯获取字典的对象，可以用values()方法获取
    # User.objects.all().values("user_name", "mail") 类似于SQL语句

    d = User.objects.all().values_list("user_name", "mail")  # values 返回的是dict，values_list返回的是元组
    sql = d.query
    r = ''
    for i in d:
        r += repr(i)
    return HttpResponse('<p>查询结果：%s</p>,'
                        '<p>%s</p>'%(r,sql))

def select_user4(request):
    e = User.objects.exclude(user_name='yoyo')
    sql = e.query
    users = ''
    psws = ''
    mails = ''
    for i in e:
        users += ' ' + i.user_name
        psws += ' ' + i.psw
        mails += ' ' + i.mail
    return HttpResponse('''<p>查询user结果：%s</p>
                        <p>查询psw结果：%s</p>
                        <p>查询psw结果：%s</p>
                        <p>sql:%s</p>''' % (users, psws, mails,sql))

def select_user5(request):
    e = User.objects.all().order_by("mail")
    sql = e.query
    users = ''
    psws = ''
    mails = ''
    for i in e:
        users += ' ' + i.user_name
        psws += ' ' + i.psw
        mails += ' ' + i.mail
    return HttpResponse('''<p>查询user结果：%s</p>
                        <p>查询psw结果：%s</p>
                        <p>查询psw结果：%s</p>
                        <p>sql:%s</p>''' % (users, psws, mails,sql))

def select_user6(request):
    e = User.objects.all().order_by("-mail").distinct()
    sql = e.query
    users = ''
    psws = ''
    mails = ''
    for i in e:
        users += ' ' + i.user_name
        psws += ' ' + i.psw
        mails += ' ' + i.mail
    return HttpResponse('''<p>查询user结果：%s</p>
                        <p>查询psw结果：%s</p>
                        <p>查询psw结果：%s</p>
                        <p>sql:%s</p>''' % (users, psws, mails,sql))

def get_json(request):
    '''返回json数据'''
    data = {}
    a = User.objects.all()
    data['code'] = 200
    data['result'] = json.loads(serializers.serialize("json",a))
    return JsonResponse(data)

def get_model_to_dict(request):
    '''把返回结果转成dict序列'''
    result = User.objects.all()
    json_list = []
    for i in result:
        json_dict = model_to_dict(i)
        json_list.append(json_dict)
    return JsonResponse(json_list,safe=False)

def json_data(request):
    '''values{}获取的可迭代的dict对象list'''
    data = {}
    result = User.objects.all().values()
    data['data'] = list(result)
    return JsonResponse(data,
                        safe=False,
                        json_dumps_params={'ensure_ascii':False})





