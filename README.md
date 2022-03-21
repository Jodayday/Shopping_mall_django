# djang를 사용한 유저,게시판 기능 작성

## [주의사항] 강의 내용을 그대로 따라하는 과정

배운걸 적용하면서 변경한내용은 branch side로 이동할것

## 1.참조사이트

[request의 속성들](https://runebook.dev/ko/docs/django/ref/request-response) :
get.post등 전송되는 값들을 담고 있다.

[페이징기능설명](https://wikidocs.net/71240) :
django.core.paginator에 Paginator 클래스를 이용해서 쉽게 구현이 된다.

[url 네임스페이스 사용](https://docs.djangoproject.com/ko/4.0/intro/tutorial03/#namespacing-url-names) :
url변경시 모든 html를 수정할 필요가 없다.

[폼 필드와 인자들](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Forms) :
error_messages와 label, widget, required를 사용했다.
cleaned_data 내용이 밑에 나오는데 폼으로 전송한 데이터를 처리한다.
cleaned_data를 이용해서 폼에 작성한 데이터를 받을수있다.

[장고의 간편하면서 편리한기능](https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/) :
render, redirect,get_object_or_404,get_list_or_404 등 있다. 이 프로젝트에선 render와 redirect 만 사용되었다.

[QuertSetAPI](https://docs.djangoproject.com/en/4.0/ref/models/querysets/) :
모델를 어떻게 다룰건지에 대해 나와있으며 all,get_or_create,get,order_by 를 사용했으며 다양한 기능이 더 있다.

## 2.현재까지의 개선을 했으면 하는점

1. 현재 이름이 중복되면 회원가입을 막았다. >> 체크할수있는 기능
2. 서버를 재시작해도 세션이 남아있다. >> 페이지를 나가면 자동로그아웃
3. 폼에서 입력후 문제로 인해 전송이 안될때 입력한 값은 남아있었으면 좋겠다.
4. 한개의 게시글을 볼때 이전과 이후 게시글로 이동할수있는 버튼
5. 게시글에 대한 공감,댓글기능
6. 작성자가 쓴글에 대한 삭제 기능
