from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login ,logout 
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from core.views import *
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.utils.translation import pgettext
from django.views.generic import FormView
from contact.forms import CustomChangePasswordForm, CustomSetPasswordForm
from contact.views import *
from django.template.loader import get_template
from contact.task import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from contact.task import send_confirmation_mail
from contact.forms import *


User = get_user_model()


class ContactPage(TemplateView, SubscriberPage):
    template_name = "contact.html"


class ContactView(CreateView, SubscriberPage):
    form_class = ContactForm
    template_name = 'contact.html'
   
    def get_success_url(self):
        return reverse_lazy('contact:contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'email/password_reset_email.html'
    form_class = CustomPasswordResetForm
    template_name = 'forget-password.html'
    success_url = reverse_lazy('contact:login')
    
    def get_success_url(self):
        messages.success(self.request, 'Your request has been considered')
        return super(CustomPasswordResetView, self).get_success_url()


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'reset_password.html'
    success_url = reverse_lazy('accounts:login')
    form_class = CustomSetPasswordForm
    
    def form_valid(self, form):
        messages.success(self.request, 'Your password has been successfully changed.')
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Your password has been successfully changed.')
        return super(CustomPasswordResetConfirmView, self).get_success_url()


class RegisterView(CreateView, SubscriberPage):
    form_class = RegistrationForm
    request_method = ['POST']
    template_name = 'register.html'
    success_url = reverse_lazy('contact:register')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('contact:login')
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        print(form.cleaned_data)
        form.save()
        form.is_active = False
        result = super().form_valid(form)
        
        user = form.instance
        send_confirmation_mail(user)
        messages.success(self.request, 'Please, confirm your e-mail address.')

        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] =  RegistrationForm()
        context['forms'] = LoginForm()
        return context
        


class CustomLoginView(LoginView, SubscriberPage):
    form_class = LoginForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('core:main')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] =  RegistrationForm()
        context['forms'] = LoginForm()
        return context




class CustomLogoutView(LogoutView):
    next_page = 'core:main'
    # def logout_view(request):
    #     logout(request)
    #     success_url = reverse_lazy('contact:main')
    #     return redirect('/login')
        

 
  


def activate(request, uidb64, token):
    uid = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.filter(pk=uid, is_active=False).first()

    if user is not None :
        messages.success(request, 'Success')
        user.is_active = True
        user.save()
        LogoutView()
        return redirect('contact:register')

    else:
        messages.error(request, 'Ooooppssss')
        return redirect('core:main')


