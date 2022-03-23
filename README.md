# django site study

## 버전

python 3.9.7
django 3.2.8

## 간단한 쇼핑몰 만들기

### models

        1.user
        > UserClass
        2.shopping
        > ProductClass, OrderClass

### urls

        1. admin
        2. user
        3. shopping

### views 구현

        1. 클래스 기반(제네릭 뷰)

### user app, 사용된 함수

        1. from django.contrib.auth.hashers import make_password
        2. form_valid 정상완료시 동작하는 함수
        > 해당함수를 이용해서 form의 값을 가져와서 세션연결함

### 사용한 기능

[내장된 클래스 기반 작성법](https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/#built-in-class-based-generic-views)
[내장 템플릿 태그 및 필터](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/)
[django.contrib.humanize](https://docs.djangoproject.com/en/4.0/ref/contrib/humanize/)
[서머노트](https://summernote.org/getting-started/#requires-html5-doctype)

> 저장을 base64 형태로 sql에 저장, 만족스럽지 못한 동작 -> 따로 폴더가 생기고 거기에 차곡차곡 이미지가 저장되었으면 좋겠음

#### 팁

        1.

"""
def get_context_data(self, **kwargs): # 값을 추가하고 싶을때
context = super().get_context_data(**kwargs)
context['form'] = OrderForm(self.request) # 폼클래스 생성하면서 request전달
return context

def get_form_kwargs(self, **kwargs): # 어떤인자값을 전달할지 설정하는 함수
kw = super().get_form_kwargs(**kwargs)
kw.update({
'request': self.request
})
return kw

"""
두개 비슷하게 사용한다.

        2.

"""
def form_valid(self, form): #성공했을때 실행
def form_invalid(self, form): #실패했을때 실행
"""
