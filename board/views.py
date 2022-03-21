from django.http import Http404
from django.shortcuts import redirect, render
from django.core.paginator import Paginator

# Create your views here.
from .models import BoardInfo
from .forms import BoardForm
from userconfig.models import UserInfo


def index(request):

    all_boards = BoardInfo.objects.all().order_by("-id")
    page = int(request.GET.get("p", 1))
    # 페이지 번호 받을변수 p
    paginator = Paginator(all_boards, 6)
    # 페이징 수
    boards = paginator.get_page(page)

    return render(request, "board/board_list.html", {"boards": boards})


def write(request,):

    if not request.session.get('user'):
        return redirect("/user/")

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


def detail(request, pk):
    try:
        model = BoardInfo.objects.get(pk=pk)
    except BoardInfo.DoesNotExist:
        raise Http404("게시글이 존재하지 않습니다.")
    return render(request, "board/board_detail.html", {"details": model})
