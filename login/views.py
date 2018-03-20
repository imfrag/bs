from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_POST
from main.models.entity import HouseHolder, Staff

# Create your views here.


# 用户登录
def signin(request, level=1):
    if level not in [1, 2, 3]:
        # 返回 404.html
        return render(request, '404.html')

    if request.method == 'GET':
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

    elif request.method == 'POST':
        # 处理post方法请求，处理客户端请求数据，并验证

        if level == 1:
            # 验证用户登录
            auth = request.POST.get('auth', '')
            if auth:
                #user = HouseHolder.objects.get(username=request.POST[
                #    'username'])

                request.session['is_login'] = 1
                #request.session['user'] = user
                return  HttpResponseRedirect(reverse('index'))
        elif level == 2:
            # 验证物业管理职员登录
            pass
        elif level == 3:
            # 验证系统管理员登录
            pass

    else:
        pass


def signup(request):

    if request.session.get('user', default=""):
        return HttpResponseRedirect(reverse('profile',
                                    username=request.session['username']))

    if request.is_ajax():
        # 异步请求，验证用户名或邮箱
        code = 1  # 通过
        username = request.GET.get('username')
        if HouseHolder.objects.get(username=username):
            username_msg = "该用户名已存在"
            code = 2  # 已存在

        email = request.GET.get('email')
        if HouseHolder.objects.get(email=email):
            email_msg = "该邮箱已被注册"
            code = 2  # 已存在

        return JsonResponse({'username_msg': username_msg,
                             'email_msg': email_msg,
                             'code': code})
    elif request.method == "POST":
        # 处理用户注册请求
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # new_user = HouseHolder(id=0,
        #                        username=username,
        #                        password=password,
        #                        email=email)
        # new_user.save()
        # request.session['user'] = new_user

        return HttpResponseRedirect(reverse('profile', args=[username]))
    elif request.method == "GET":
        # 返回注册页面
        return render(request, 'login/signup.html')


@require_POST
def logout(request):
    pass
