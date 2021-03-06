from django import forms

from user.models import User
from django.contrib.auth.hashers import check_password


class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': "이메일을 입력해주세요"
        },
        label="이메일",
        max_length=64,
    )
    password = forms.CharField(
        error_messages={
            'required': "비밀번호을 입력해주세요"
        },
        label="비밀번호",
        widget=forms.PasswordInput,
    )

    repassword = forms.CharField(
        error_messages={
            'required': "비밀번호을 입력해주세요"
        },
        label="비밀번호 확인",
        widget=forms.PasswordInput,
    )

    def clean(self):
        cleaned_data = super().clean()

        _e1 = cleaned_data.get("email")
        _p1 = cleaned_data.get("password")
        _p2 = cleaned_data.get("repassword")

        if _p1 and _p2:
            if _p1 != _p2:
                self.add_error("repassword", '비밀번호가 다릅니다.')


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': "이메일을 입력해주세요"
        },
        label="이메일",
        max_length=64,
    )
    password = forms.CharField(
        error_messages={
            'required': "비밀번호을 입력해주세요"
        },
        label="비밀번호",
        widget=forms.PasswordInput,
    )

    def clean(self):
        cleaned_data = super().clean()

        _e1 = cleaned_data.get("email")
        _p1 = cleaned_data.get("password")

        if _e1 and _p1:
            try:
                _u = User.objects.get(email=_e1)
            except User.DoesNotExist:
                self.add_error("email", "가입정보가 없습니다.")
                return
            except User.MultipleObjectsReturned:
                self.add_error("email", "중복가입된 사용자 입니다.")
                return
            if not check_password(_p1, _u.password):
                self.add_error("email", "가입정보가 없습니다..")
            # else:
                # self.user = _u.id
                # self.user --> views.LoginView의 form.user로 사용된다.
