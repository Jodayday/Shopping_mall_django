from django.shortcuts import redirect, render

from django.views.generic import FormView
from django.contrib.auth.hashers import make_password
# Create your views here.

from user.forms import RegisterForm, LoginForm
from user.models import User


def index(request):
    context = {'user': request.session.get('user', "why?")}
    return render(request, "user/index.html", context)


class RegisterView(FormView):
    template_name = "user/register.html"
    # 사용할 템플릿 선정
    form_class = RegisterForm
    # 사용할 폼 선정
    success_url = '/'
    # 성공적으로 완료시 이동화면

    def form_valid(self, form):
        # 폼의 유효성 검사가 끝났을때 동작
        user = User(
            email=form.data.get("email"),
            password=make_password(form.data.get("password")),
            # 폼에서 전달한 데이터위치는 form.data에 있음
            level='buyer'
        )
        user.save()
        return super().form_valid(form)


class LoginView(FormView):
    template_name = "user/login.html"
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        user1 = form.data.get("email")
        user = User.objects.get(email=user1)
        self.request.session['user'] = user.pk
        # self안에 request가 존재,    formClass에서 가져온 값
        return super().form_valid(form)


def logout(request):
    del request.session['user']
    return redirect("/")
