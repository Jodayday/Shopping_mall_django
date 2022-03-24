from django.shortcuts import redirect
from django.urls import reverse

from user.models import User


def login_required(fun):
    # 랩핑한 함수와 기존인자값을 맞춰주어야 에러가 안발생함
    def wrap(request, *args, **kwargs):
        user = request.session.get("user")
        if user is None and not user:
            return redirect(reverse("user:login"))
        return fun(request, *args, **kwargs)
    return wrap


def login_level(fun):
    def wrap(request, *args, **kwargs):
        user_pk = request.session.get("user")
        if user_pk is None and not user_pk:
            return redirect(reverse("user:login"))

        user = User.objects.get(pk=user_pk)
        if user.level != 'admin':
            return redirect(reverse("index"))
        return fun(request, *args, **kwargs)
    return wrap
