from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from polls.models import Article
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail,send_mass_mail
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

# Create your views here.
def index(request):
    return HttpResponse("你好啊，傻孩子")

def demo(request):
    return render(request,'demo.html')

def page(request,num):
    try:
        return render(request, 'demo.html')
    except:
        raise Http404

def home2(request,year,month):
    return HttpResponse("获取当前页面的home的时间标签：%s年-%s月"%(year,month))

def home1(request,year,month):
    return HttpResponse("获取当前页面的home的时间标签：%s年-%s月"%(year,month))
def home(request):
    return render(request,'home.html')

@login_required(login_url='/login')
def leslie(request):
    context = {}
    context['name'] = '马克华菲'
    return render(request,'leslie.html',context)

def sonpage(request):
    context = {"ads":["selenium","appium","requests"]}
    return render(request,'sonpage.html',context)

# 测试qq号访问页面
def test_qq(request):
    return render(request,'get_demo.html')

# 提交后返回页面
def result_qq(request):
    if request.method == 'GET':
        r = request.GET.get('q',None) # r = request.GET['q']
        res = ''
        try:
            if int(r) %2:
                res = "大吉大利!"
            else:
                res = "恭喜发财！"
        except:
            res = "请输入正确的qq号码！"
        return HttpResponse("测试结果是: %s"%res)
    else:
        return render(request,'test_qq.html')

def select_mail(request):
    res = ''
    if request.method == 'GET':
        r = request.GET.get('name',None)
        if r:
            res = User.objects.filter(username="%s"%r)
            try:
                res = res[0].email
            except:
                res = "没有查询到信息"
            return render(request,'name.html',{'email':res})
        else:
            return render(request,'name.html',{'email':res})
    else:
        return render(request,'name.html',{"email":"请求方法有误!"})

def register(request):
    res = ''
    if request.method == 'POST':
        user_name = request.POST.get('username')
        psw = request.POST.get('password')
        mail = request.POST.get('email')
        # 先查询数据库中有没有，有的话说明已经注册了
        user_list = User.objects.filter(username=user_name)
        if user_list:
            # 如果已经注册给个提示信息
            rename = "%s用户已经注册过了"%user_name
            return render(request,'register.html',{'rename':rename})
        else:
            # 如果没有注册，则插入数据库
            sql = User.objects.create_user(username=user_name,password=psw,email=mail)
            sql.save()
            return HttpResponseRedirect('/login')
    return render(request,'register.html')
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                request.session['user'] = username
                return HttpResponseRedirect('/leslie')
            else:
                error = "用户不存在"
                return render(request,'login.html',{'error':error})
        else:
            error = "用户名或密码不正确"
            return render(request, 'login.html', {'error': error})
    return render(request,'login.html')
def s_mail(request):
    send_mail('这是主题',
              '这是正文',
              'test616387@126.com',
              ['616387521@qq.com'],
              fail_silently=False
              )
    return HttpResponse("邮件发送成功！")

def s_mass_mail(request):
    message1 = ('这是主题1',
              '这是正文',
              'test616387@126.com',
              ['616387521@qq.com']
              )
    message2 = ('这是主题2',
                '这是正文',
                'test616387@126.com',
                ['616387521@qq.com']
                )
    message3 = ('这是主题3',
                '这是正文',
                'test616387@126.com',
                ['616387521@qq.com']
                )
    send_mass_mail((message1,message2,message3),
              fail_silently=False
              )
    return HttpResponse("邮件发送成功！")

def reset_psw(request):
    res = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')

        # 如果新旧密码一致则不允许修改
        if password == new_password:
            res = "新旧密码一致，无需修改"
            return render(request,'reset_psw.html',{"msg":res})
        else:
            user = authenticate(username=username,password=password)
            if user is not None:
                user.set_password(new_password)
                user.save()
                res = '密码修改成功'
            else:
                res = '密码错误'
            return render(request,'reset_psw.html',{"msg":res})
    else:
        return render(request,'reset_psw.html',{'msg':res})



