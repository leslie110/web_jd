from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from hehe import models
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def hehe_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                request.session['user'] = username
                return HttpResponseRedirect('/hehe/logon')
                # return HttpResponse('登陆成功')
            else:
                content = {
                    'error':'账号权限异常'
                }
                return render(request,'hehe_login.html',content)
        else:
            content = {
                'error': '账号或者密码不正确'
            }
            return render(request,'hehe_login.html',content)
    else:
        content = {'error':'',
                   'title':'boot登录系统'}
        return render(request,'hehe_login.html',content)
@login_required(login_url='/hehe/login')
def hehe_logon(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user_list = User.objects.filter(username=username)
        if user_list:
            content = {
                'error':"用户名已存在"
            }
            return render(request,'hehe_logon.html',content)
        else:
            content = {
                'error': "添加成功"
            }
            user = User.objects.create_user(username,password,email)
            user.save()
            return render(request,'hehe_logon.html',content)
    else:
        content = {'error': '',
                   'title': 'boot添加用户'}
        return render(request,'hehe_logon.html',content)

@login_required(login_url="/hehe/login")
def hehe_reset_psw(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')

        # 如果新旧密码一致则不允许修改
        if password == new_password:
            res = "新旧密码一致，无需修改"
            return render(request,'hehe_rest_psw.html',{"error":res})
        else:
            user = authenticate(username=username,password=password)
            if user is not None:
                user.set_password(new_password)
                user.save()
                res = '密码修改成功'
            else:
                res = '密码错误'
            return render(request,'hehe_rest_psw.html',{"error":res})
    else:
        content = {'error': '',
                   'title': 'boot修改密码'}
        return render(request,'hehe_rest_psw.html',content)



