from django.shortcuts import render, redirect, reverse
from project.utils import get_user, get_sk
from shop.order.models import Order
from django.shortcuts import get_object_or_404
from django.contrib import messages 
from django.utils.translation import gettext as _


def update_profile(request):
  first_name   = request.POST['first_name']
  last_name    = request.POST['last_name']
  phone_number = request.POST['phone_number']
  email        = request.POST['email']
  user = request.user
  user.first_name=first_name
  user.last_name = last_name
  user.phone_number = phone_number
  user.email = email
  user.save()
  messages.success(request, 'Ваші данні були оновлені')
  print(request.user)
  return redirect('profile')


# @login_required
def delete_order(request, pk):
  order = get_object_or_404(
    Order,
    pk=pk,
    user=get_user(request),
  )
  order.delete()
  messages.success(request, _('order was deleted'))
  return redirect('profile')

