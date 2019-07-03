from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.template import loader
from django.views.generic import UpdateView
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator

def home(request):
    return render(request, 'accounts/account.html')

# def logout(request):
#     return render(request, 'accounts/account.html')

def profile(request):
    return redirect('/accounts')

def signup(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, f'Account {user.username} is created and logged in, Enjoy!')
            return redirect('/accounts')
        #else:
            #return HttpResponse('Loi cmnr')
            # return redirect('/accounts')
    else:
        form = SignUpForm()
        # form = UserCreationForm()
        
    return render(request, 'accounts/signup.html', {'form': form})

class UserUpdateView(UpdateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'date_joined' )
    template_name = 'accounts/update.html'
    success_url = reverse_lazy('accounts:update')

    def get_object(self, request):
        return self.request.user