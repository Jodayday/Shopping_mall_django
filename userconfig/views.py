
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.hashers import make_password, check_password
# 패스워드 생성과 체크
# Create your views here.
from .models import UserInfo
from .forms import LoginForm


def index(request):
    return render(request, "userconfig/index.html")


def register(request):
    """
    로그인 페이지에 2가지 요청이 들어옴 
    링크타고 들어온것과 값을 작성해서 전송한것
    """
    if request.method == "GET":
        return render(request, "userconfig/register.html")
    elif request.method == "POST":
        username = request.POST.get("username", None)
        # get으로 가져옴 key값을 찾고 없으면 None 반환
        useremail = request.POST.get("useremail", None)
        password = request.POST.get("password", None)
        repassword = request.POST.get("repassword", None)
        # 입력받은 값을 가져옴 form의 input의 name명임
        message = {}
        try:
            temp_name = UserInfo.objects.get(user_name=username)
        except (UserInfo.MultipleObjectsReturned, UserInfo.DoesNotExist):
            if username and password and repassword and useremail:
                # 필요한 추가정보 전달
                "모두 입력 했을때"
                if password == repassword:
                    "비번이 같을때"
                    model = UserInfo(
                        user_name=username,
                        user_email=useremail,
                        password=make_password(password),
                    )
                    # 객체 생성
                    model.save()
                    # 객체를 모델에 저장
                    return redirect("/")
                else:
                    message['error'] = "비밀번호가 서로 다릅니다."
            else:
                message['error'] = "값을 입력해주세요"

            return render(request, "userconfig/register.html", message)
        if temp_name:
            message['error'] = "중복이름이 존재합니다."
        return render(request, "userconfig/register.html", message)


def login(request):
    """
    로그인 체크 함수 
    """
    if request.method == "GET":
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user
            return redirect('/')

    return render(request, "userconfig/login.html", {"form": form})


def logout(request):
    if request.session.get('user'):
        del request.session['user']
    return redirect("/")
