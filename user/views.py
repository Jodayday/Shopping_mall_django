from django.shortcuts import render

from django.views.generic import FormView
# Create your views here.

from user.forms import RegisterForm, LoginForm


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


class LoginView(FormView):
    template_name = "user/login.html"
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.user
        return super().form_valid(form)
