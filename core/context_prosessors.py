from core.form import SubscribeForm
from core.models import Subscriber
from store.form import ReviewForm
from store.models import Review


def subscribe(request):
    form = SubscribeForm(request.POST or None)
    if request.method == "POST" :
        if  form.is_valid():
            form.save()
    return {'subscriber_form' : form}


def reviews(request):
    form = ReviewForm(request.POST or None)
    if request.method == "POST" :
        if  form.is_valid():
            form.save()
    return {'review_form' : form}


  