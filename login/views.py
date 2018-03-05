from django.shortcuts import render
from django.views.decorators.http import require_POST

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
            pass
        elif level == 2:
            # 验证物业管理职员登录
            pass
        elif level == 3:
            # 验证系统管理员登录
            pass

    else:
        pass


def signup(request):

    if request.method == "GET":
        # 返回注册页面
        pass
    elif request.method == "POST":
        # 处理用户注册请求
        pass


@require_POST
def logout(request):
    pass
