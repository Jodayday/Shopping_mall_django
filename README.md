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
[REST_framework](https://www.django-rest-framework.org/)

> 저장을 base64 형태로 sql에 저장, 만족스럽지 못한 동작 -> 따로 폴더가 생기고 거기에 차곡차곡 이미지가 저장되었으면 좋겠음

[트렌젝션 처리](https://docs.djangoproject.com/en/4.0/topics/db/transactions/#controlling-transactions-explicitly)

#### 팁

1.                     """
          def get_context_data(self, **kwargs): # 값을 추가하고 싶을때
          context = super().get_context_data(**kwargs)
          context['form'] = OrderForm(self.request) # 폼클래스 생성하면서 request전달
          return context

          def get_form_kwargs(self, **kwargs):
          # 어떤인자값을 전달할지 설정하는 함수
          kw = super().get_form_kwargs(**kwargs)
          kw.update({
          'request': self.request
          })
          return kw

          """

두개 비슷하게 사용한다.

2.              """
          form class

          def form_valid(self, form): #성공했을때 실행
          def form_invalid(self, form): #실패했을때 실행
          """

3.              """
          #클래스 상속시 django는 지원한다.
          from django.utils.decorators import method_decorator
          @method_decorator(login_level, name="dispatch")
                          # 함수          ,적용할 함수명
          """
          dispatch 함수는 클래스 호출시(화면호출) 동작하는 함수
          login_level은 역할을 확인하는 함수
          """

          """

4.            """
        오버라이딩
        기존함수에서 추가적인 동작을 요할때

        ex)1
        def form_valid(self, form):
            with transaction.atomic():
                # db 트렌젝션 설정
                p = Product.objects.get(pk=form.data.get("product"))
                order = Order(
                    user=User.objects.get(pk=self.request.session.get('user')),
                    product=p,
                    quantity=form.data.get("quantity"),
                )
                order.save()
                p.stock -= int(form.data.get("quantity"))
                p.save()
            return super().form_valid(form)

        ex)2
        def get_form_kwargs(self, **kwargs):
            kw = super().get_form_kwargs(**kwargs)
            kw.update({
                'request': self.request
            })
            return kw

        super에서 실행후 추가하거나
        추가하고 super에서 실행하거나


        """

5.         """
        Restful API는 REST 특징을 지키면서 API를 제공
        [RESTAPI 기본설명](https://team-platform.tistory.com/36)
        REST_API 구현 가이드라인
        1.URL은 정보의 자원으로 표시할것, 명사/지정/명사 까지만 사용을 권장
        ex) products/1/orders
        어쩔수없이 동사 사용시 자원명 뒤에 콜론(:)을 넣고 뒤에 동사
        ex) products:create

        2. post, get, put , delete 등 method의 행위로 표현
        post:생성,
        get:검색
        put:업데이트
        delete:삭제
        """
