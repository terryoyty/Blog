from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

from user.forms import UserLoginForm, UserRegisterForm


class RegisterView(View):

    def get(self, request):
        user_register_form = UserRegisterForm()
        return render(request, 'user/register.html', {'form': user_register_form})

    def post(self, request):
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            # 设置密码
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            # 保存好数据后立即登录并返回博客列表页面
            login(request, new_user)

            messages.add_message(request, messages.SUCCESS, '注册成功', extra_tags='success')

            return redirect("app:index")

        messages.add_message(request, messages.ERROR, '注册失败', extra_tags='danger')
        return render(request, 'user/register.html', {
            'form': user_register_form,
        })


class LoginView(View):

    def get(self, request):
        user_login_form = UserLoginForm()
        return render(request, 'user/login.html', {'form': user_login_form})

    def post(self, request):
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            data = user_login_form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # 将用户数据保存在 session 中，即实现了登录动作
                login(request, user)
                messages.add_message(request, messages.SUCCESS, '登陆成功', extra_tags='success')
                return redirect("app:index")
            else:
                messages.add_message(request, messages.ERROR, '账号或密码输入有误, 请重新输入。', extra_tags='danger')
                return render(request, 'user/login.html', {'form': user_login_form})
        else:
            messages.add_message(request, messages.ERROR, '账号或密码输入不合法', extra_tags='danger')
            return render(request, 'user/login.html', {'form': user_login_form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        messages.add_message(request, messages.ERROR, '注销成功', extra_tags='success')
        return redirect("app:index")