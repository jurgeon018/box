from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect 
from .utils import create_liqpay_transaction

@csrf_exempt
def pay_callback(request):
  create_liqpay_transaction(request)
  return redirect('thank_you')


from django.http import HttpResponse 


from django.shortcuts import render 


def test_part(request):
  return render(request, 'liqpay/test_part.html', locals())


