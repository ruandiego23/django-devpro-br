
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from devpro.base.forms import UserForm
from devpro.base.models import User


# Create your views here.
def home(request):
    return render(request, 'base/home.html')


def sign_up(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return HttpResponseRedirect('/modulos/')
            else:
                ctx = {'form': form}
                return render(request, 'registration/sign-up.html', ctx)
        else:
            login(request, user)
            return HttpResponseRedirect(reverse('base:home'))

    return render(request, 'registration/sign-up.html')
