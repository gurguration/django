from django.conf.urls import url
from .views import DiscountApply


app_name = 'coupons'

urlpatterns = [
    url(r'^apply', DiscountApply, name='apply')
]
