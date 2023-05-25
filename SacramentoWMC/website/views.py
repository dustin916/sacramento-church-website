# django imports
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect # HttpResponseRedirect redirect back to the page itself
from django.core.mail import send_mail
from django.contrib import messages



# other imports

# Import Pagination Stuff
from django.core.paginator import Paginator, EmptyPage


import os
# local imports
from .models import Sermon
from .forms import SermonForm, ContactForm


# Create your views here.


def home(request):
    from website.namer import namer
    return render(request, 'website/home.html', {
        "my_stuff": namer,
        })

#About Us

def about(request): 
    title = "Who We Are"
    return render(request, 'website/about.html', {
        "title": title
    })
    
def faith(request): # Articles of Faith
    title = "Articles of Faith"
    return render(request, 'website/faith.html', {
        "title": title
    })
# Sermons

def sermon_list(request):
    # Sermons (Database)
    sermons = Sermon.objects.all().order_by('-date') # can add more filters. add , 'next filter' - if you put '?' it will be randomized each time
    sermon_dir = 'media/'
    
    # Set up Pagination
    p = Paginator(Sermon.objects.all().order_by('-date'), 10)
    page = request.GET.get('page')  
    sermon_page = p.get_page(page)
    nums = "a" * sermon_page.paginator.num_pages


    return render(request, 'website/sermon_list.html', {
        'sermons': sermons,
        'sermon_dir': sermon_dir,
        'sermon_page': sermon_page,
        'nums': nums,

    })

def add_sermon(request):
    submitted = False
    if request.method == 'POST':
        form = SermonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add-sermon?submitted=True')
    else:
        form = SermonForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'website/add_sermon.html', {
        'form': form,
        'submitted': submitted
    })

def delete_sermon(request, sermon_id):
    sermon = Sermon.objects.get(pk=sermon_id)
    if request.user.is_authenticated:
        sermon.delete()
        messages.success(request, ('Sermon has been deleted.'))
        return redirect('sermon-list')
    else:
        messages.success(request, ('You are not authorized to access this page.'))
        return redirect('sermon-list')

# individual sermon page

def sermon(request, sermon_id):
    sermon = Sermon.objects.get(pk=sermon_id)
    sermons = Sermon.objects.all().order_by('-date')
    sermon_dir = 'media/'

    # Set up Pagination
    p = Paginator(Sermon.objects.all().order_by('-date'), 5) # the 5 is how many items per page we want.
    page = request.GET.get('page')
    sermon_page = p.get_page(page)

    return render(request, 'website/sermon.html', {
        'sermon': sermon,
        'sermon_dir': sermon_dir,
        'sermons': sermons,
        'sermon_page': sermon_page,
    })

def search_sermons(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        sermons = Sermon.objects.filter(speaker__contains=searched) # try sermons = Sermon.objects(searched) 
        return render(request, 'website/search_sermons.html', {
            'searched': searched,
            'sermons': sermons,

        })
    else:
        return render(request, 'website/search_sermons.html', {
            
        })

# Contact

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message_subject = form.cleaned_data['subject']
            message_name = form.cleaned_data['name']
            message_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
    
    
            message_to_me = "Name: " + message_name + "\n" + "From: " + message_email + ": " + "\n" + "Message: " + "\n" + message

            response_email = "Thank you for contacting me. If you received this email that means we received your message. We will respond shortly."
            
            
            # Send an email
            send_mail(
                '{}'.format(message_subject), # subject
                message_to_me, # message
                message_email, # from email (who is filling out the form)
                ['sacramentowmc@gmail.com'], # To email (where is the form being sent to)
            )
            # Confirmation email
            send_mail(
                'Confirmation', # subject
                response_email, # message
                'sacramentowmc@gmail.com', 
                [message_email], 
            )
            return render(request, 'website/contact.html', {
                "message_name": message_name,

            })
        else:
            form = ContactForm(initial={
                'subject': request.POST.get('subject', ''),
                'name': request.POST.get('name', ''),
                'email': request.POST.get('email', ''),
                'message': request.POST.get('message', ''),
            })


            messages.success(request, ('Please verify that you are human by clicking the check box and try again.'))
    else:
        form = ContactForm()
        
    return render(request, 'website/contact.html', {
        "form": form,

    })

    

