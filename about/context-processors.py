from about.forms import *
from about.models import *

def billing(request):
    form = BillingData(request.POST or None)
    if request.method == "POST" :
        if  form.is_valid():
            form.save()
    return {'billingdata_form' : form}

# def shipping(request):
#     form = Shipping_info(request.POST or None)
#     if request.method == "POST" :
#         if  form.is_valid():
#             form.save()
#     return {'shipping_form' : form}