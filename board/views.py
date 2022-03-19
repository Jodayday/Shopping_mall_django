from django.shortcuts import redirect, render

# Create your views here.
from .models import BoardInfo
from .forms import BoardForm
from userconfig.models import UserInfo


def index(request):
    boards = BoardInfo.objects.all().order_by("-id")

    return render(request, "board/board_list.html", {"boards": boards})


def write(request,):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            user_session = request.session.get('user')
            user = UserInfo.objects.get(pk=user_session)

            board = BoardInfo()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = user
            board.save()
            return redirect("/board/")
    else:
        form = BoardForm()

    return render(request, "board/board_write.html", {"form": form})
