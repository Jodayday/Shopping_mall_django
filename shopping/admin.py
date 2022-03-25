from django.contrib import admin

from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType
# 장고의 액션에 대한 로그를 남기기위한 모듈

from django.utils.html import format_html
# Register your models here.
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db.models import Q
# 필터에 일괄적으로 값 적용
from django.db import transaction
# import models
from .models import Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", 'price_style', 'stock_style', "stock_status",)
    search_fields = ("name", "price",)

    def changelist_view(self, request, extra_context=None):
        extra_context = {"title": "상품 목록"}
        return super().changelist_view(request, extra_context)

    def change_view(self, request, object_id=None, form_url='', extra_context=None):
        product = Product.objects.get(pk=object_id)
        extra_context = {'title': f'{product.name} 수정'}
        return super().change_view(request, object_id, form_url, extra_context)

    def stock_style(self, obj):
        stock = intcomma(obj.stock)
        return f"{stock} 개"
    stock_style.short_description = "가격"

    def price_style(self, obj):
        price = intcomma(obj.price)
        return f"{price} 원"
    price_style.short_description = "가격"

    def stock_status(self, obj):
        if obj.stock < 2:
            return format_html(f"<b style='color:red;'>{obj.stock}</b>")
        elif obj.stock < 5:
            return format_html(f"<b style='color:green;'>{obj.stock}</b>")
        else:
            return format_html(f"<b>{obj.stock}</b>")

    stock_status.short_description = "재고상태"
    # 함수의 헤더표시를 변경
# 액션의 이름 설정


@admin.action(description='환불하기')
def refund(self, request, queryset):
    # queryset엔 체크한 애들이 들어옴
    with transaction.atomic():
        query1 = queryset.filter(~Q(status="환불"))
        content1 = ContentType.objects.get_for_model(queryset.model)
        # 컨텐츠 타입가져오기
        for query in query1:
            query.product.stock += query.quantity
            query.product.save()

            # 로그적용
            LogEntry.objects.log_action(
                user_id=request.user.id,
                # 사용자
                content_type_id=content1.pk,
                # 모델의 타입
                object_id=query.pk,
                # 해당 제품
                object_repr=f"{query.product.name} 환불처리",
                # 링크 제목
                action_flag=CHANGE,
                # 1:추가(ADDTION), 2:변경(CHANGE), 3:삭제(DELETION)
                change_message="주문환불",
            )

        query1.update(status="환불")

    # 액션의 동작시 수량 반환


class OrderAdmin(admin.ModelAdmin):
    list_filter = ("status",)
    # 필터 생성
    list_display = ("user", 'product', "quantity", 'styled_status', "button")

    change_list_template = "order/order_change_list.html"
    # list의 기본 템플릿을 변경함
    actions = [
        refund,
        "dhks"
    ]

    def dhks(self, request, queryset):

        for query in queryset:
            LogEntry.objects.log_action(
                user_id=request.user.id,
                content_type_id=ContentType.objects.get_for_model(
                    queryset.model).pk,
                object_id=query.pk,
                object_repr=f"{query.product.name} 결제완료",
                action_flag=2,

            )

        queryset.update(status="결제완료")

    def changelist_view(self, request, extra_context=None):
        """내장된 함수 오버라이딩하여 list의 제목을 변경"""
        extra_context = {"title": "주문 목록"}

        if request.method == "POST":
            with transaction.atomic():
                obj_id = request.POST.get('obj_id')
                # if obj_id:
                query1 = Order.objects.filter(pk=obj_id)
                content1 = ContentType.objects.get_for_model(query1.model)
                # 컨텐츠 타입가져오기
                for query in query1:
                    print(query1)
                    print(type(query))
                    print(query)
                    query.product.stock += query.quantity
                    query.product.save()

                    # 로그적용
                    LogEntry.objects.log_action(
                        user_id=request.user.id,
                        # 사용자
                        content_type_id=content1.pk,
                        # 모델의 타입
                        object_id=request.POST.get('obj_id'),
                        # 해당 제품
                        object_repr=f"{query.product.name} 환불처리",
                        # 링크 제목
                        action_flag=CHANGE,
                        # 1:추가(ADDTION), 2:변경(CHANGE), 3:삭제(DELETION)
                        change_message="주문환불",
                    )

                query1.update(status="환불")

        return super().changelist_view(request, extra_context)

    def change_view(self, request, object_id=None, form_url='', extra_context=None):
        """내장된 함수 오버라이딩하여 개별의 제목을 변경"""
        order = Order.objects.get(pk=object_id)
        extra_context = {
            'title': f'{order.user.email}의 {order.product.name} 주문정보 수정키랏'}
        return super().change_view(request, object_id, form_url, extra_context)

    @admin.display(description="상태",)
    def styled_status(self, obj):
        # 함수를 만들어 등록가능
        if obj.status == "환불":
            return format_html(f"<b style='color:red;'>{obj.status}</b>")
        elif obj.status == "결제완료":
            return format_html(f"<b style='color:green;'>{obj.status}</b>")
        else:
            return format_html(f"<b>{obj.status}</b>")

    def button(self, obj):
        if obj.status == "결제완료":
            return format_html(f"<input type='button' onclick='order_refund_submit({obj.id})' value='환불'>")
    button.short_description = "환불버튼"


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
