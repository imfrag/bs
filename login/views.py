from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_POST
from main.models.entity import HouseHolder, Staff
from django.core import serializers
import json

# Create your views here.


# 用户登录
def signin(request, level=1):
    if level not in [1, 2, 3]:
        # 返回 404.html
        return render(request, '404.html')

    if request.session.get('user', ''):
        return HttpResponseRedirect(reverse('profile',
                            args=(request.session['user']['username'],)))

    if request.is_ajax():
        '''
            前端通过ajax向后端发送异步请求，验证该用户名是否存在，和用户名与密码是否一致
            若存在且密码正确，返回json，code=1
            若存在但密码不正确，返回json，code=2
            若不存在，返回json，code=2
        '''
        username = request.GET['username']
        password = request.GET['password']

        try:
            user = HouseHolder.objects.get(username=username)
            if user.password == password:
                return JsonResponse({'username_msg': '',
                                     'password_msg': '',
                                     'code': 1})
            else:
                return JsonResponse({'username_msg': '',
                                     'password_msg': '密码与用户名不匹配',
                                     'code': 2})
        except Exception as e:
            print(e)
            return JsonResponse({'username_msg': '该用户名不存在',
                                 'password_msg': '密码与用户名不匹配',
                                 'code': 2})
    elif request.method == 'POST':
        # 处理post方法请求，处理客户端请求数据，并验证

        if level == 1:
            # 验证用户登录
            username = request.POST['username']
            user_queryset = HouseHolder.objects.filter(username=username)
            data = serializers.serialize('json', user_queryset)
            data_json = json.loads(data[1:-1])
            request.session['user'] = data_json['fields']
            request.session['userid'] = user_queryset[0].householder_id
            # request.session['level'] = user_queryset[0].level
            return HttpResponseRedirect(reverse('profile', args=(username,)))
        elif level == 2:
            # 验证物业管理职员登录
            pass
        elif level == 3:
            # 验证系统管理员登录
            pass

    elif request.method == 'GET':
        # 处理get方法请求，返回登录界面
        if level == 1:
            # 返回用户登录页面 login_user.html
            return render(request, 'login/user_signin.html')
        elif level == 2:
            # 返回物业管理页面 login_manage.html
            return render(request, 'login/manage_signin.html')
        elif level == 3:
            # 返回系统管理页面 login_admin.html
            return render(request, 'login/admin_signin.html')


def signup(request):

    if request.session.get('user', ''):
        return HttpResponseRedirect(reverse('profile',
                            args=(request.session['user']['username'],)))

    if request.session.get('username', default=""):
        return HttpResponseRedirect(reverse('profile',
                                    username=request.session['username']))

    if request.is_ajax():
        # 异步请求，验证用户名或邮箱
        code = 1  # 通过
        username_msg = ""
        email_msg = ""
        try:
            username = request.GET.get('username')
            if HouseHolder.objects.get(username=username):
                username_msg = "该用户名已存在"
                code = 2  # 已存在
        except Exception as e:
            print(e)

        try:
            email = request.GET.get('email')
            if HouseHolder.objects.get(email=email):
                email_msg = "该邮箱已被注册"
                code = 2  # 已存在
        except Exception as e:
            print(e)

        return JsonResponse({'username_msg': username_msg,
                             'email_msg': email_msg,
                             'code': code})
    elif request.method == "POST":
        # 处理用户注册请求

        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        new_user = HouseHolder(username=username,
                               password=password,
                               email=email)
        new_user.save()
        request.session['userid'] = new_user.householder_id
        user_queryset = HouseHolder.objects.filter(username=username)
        data = serializers.serialize('json', user_queryset)
        data_json = json.loads(data[1:-1])
        request.session['user'] = data_json['fields']

        return HttpResponseRedirect(reverse('profile', args=(username,)))
    elif request.method == "GET":
        # 返回注册页面
        return render(request, 'login/signup.html')


def logout(request):
    if not request.session['user']:
        return HttpResponseRedirect(reverse('index'))

    del request.session['user']
    return HttpResponseRedirect(reverse('signin', args=(1,)))
