from typing import Any, Dict
import stripe
from django.shortcuts import render,redirect
from django.conf import settings
from django.views.generic import TemplateView
from django.views import View
from django.http import JsonResponse



def payment(request):
    return render(request,'payment.html/')
def error(request):
    return render(request,'error.html/')
def charge(request):
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            intent = stripe.PaymentIntent.create(
                amount=1099,
                currency= 'inr',
                automatic_payment_methods={"enabled":True},

            )
        except stripe.error.StripeError as e:
        
         return render(request,'error.html/', {'message':'Transaction failed'})
        
    return render(request, 'charge.html')

class PaymentPageView(TemplateView):
     template_name="payment.html"
     

     def get_context_data(self, **kwargs: Any) :
         context = super(PaymentPageView, self).get_context_data(**kwargs)
         context.update({
             "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
         })
         return context



    