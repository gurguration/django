from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Discount
from .forms import DiscountApllyForm


@require_POST
def DiscountApply(request):
    discount_nmb = DiscountApllyForm(request.POST)
    if discount_nmb.is_valid():
        discount_percent = discount_nmb.cleaned_data['_ფასდაკლების_პროცენტი']

        try:
            discount_obj= Discount.objects.create(active=True, discount=discount_percent)
            # discount_obj = Discount.objects.get(active__exact='True')
            request.session['discount_id'] = discount_obj.id
        except Discount.DoesNotExist:
            print('failed')
            request.session['discount_id'] = None
    return redirect('cart:CartDetail')
