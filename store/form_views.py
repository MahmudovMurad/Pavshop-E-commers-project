from django import forms
from django.utils.translation import pgettext
from django.views.generic import FormView
from store.form import *

class ReviewView(FormView):
    template_name = "product-detail.html"
    form_class = ReviewForm
    success_url = "/"

    def form_valid(self, form):
        r = super().form_valid(form)
        print(forms.clean_data)
        return r

