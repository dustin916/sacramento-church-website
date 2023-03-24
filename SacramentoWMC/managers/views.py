from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import RegisterManagerForm

church = 'Sacramento Wesleyan Methodist Church'

def login_manager(request): # cannot def as login because we are importing login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('There was an error logging in. Try again.'))
            return redirect('login')

    else:

        return render(request, 'authenticate/login.html', {})

def logout_manager(request):
    logout(request)
    messages.success(request, ('You have been logged out sucessfully.'))
    return redirect('home')

### This can be used if the client wants it. Otherwise I will add people manually. 

#def register_manager(request):
#    if request.method == 'POST':
#        form = RegisterManagerForm(request.POST)
#        if form.is_valid():
#            form.save()
#            username = form.cleaned_data['username']
#            password = form.cleaned_data['password1']
#            manager = authenticate(username=username, password=password)
#            login(request, manager)
#            messages.success(request, ('You have been sucessfully registered as a manager of the {} website.').format(church))
#            return redirect('home')
#    else:   
#        form = RegisterManagerForm()
#    return render(request, 'authenticate/register_manager.html', {
#        'form': form,
#    })
