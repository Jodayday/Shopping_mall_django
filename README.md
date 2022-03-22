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

        0. 함수 기반
        1. 클래스 기반(제네릭 뷰)

### user app, 사용된 함수

        1. from django.contrib.auth.hashers import make_password
        2. (내장된 클래스 기반 작성법)[https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/#built-in-class-based-generic-views]
        3. form_valid 정상완료시 동작하는 함수
        > 해당함수를 이용해서 form의 값을 가져와서 세션연결함
