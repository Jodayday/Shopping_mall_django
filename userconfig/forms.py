from django import forms
from .models import UserInfo
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):

    username = forms.CharField(
        error_messages={
            'required': "아이디를 입력해주세요"
        },
        max_length=64, label="사용자이름",)
    password = forms.CharField(
        error_messages={
            'required': "비밀번호를 입력해주세요"
        },
        max_length=64, label="비밀번호", widget=forms.PasswordInput)

    def clean(self):
        """
        만들어진 함수 기존의 클린함수로 값을 가져옴
        """
        cleaned_date = super().clean()
        username = cleaned_date.get("username")
        password = cleaned_date.get("password")

        if username and password:
            try:
                user = UserInfo.objects.get(user_name=username)
            except UserInfo.DoesNotExist:
                self.add_error("username", "가입하신 정보가 없거나 비밀번호가 틀렸습니다.")
                return
            except UserInfo.MultipleObjectsReturned:
                self.add_error("username", "같은 이름이 있습니다.")
                return
            if not check_password(password, user.password):
                self.add_error("username", "가입하신 정보가 없거나 비밀번호가 틀렸습니다.")
            else:
                self.user = user.id
