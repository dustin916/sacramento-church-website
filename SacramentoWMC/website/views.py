# django imports
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect # HttpResponseRedirect redirect back to the page itself
from django.core.mail import send_mail
from django.contrib import messages

# other imports
from calendar import HTMLCalendar, month_name
from datetime import datetime

# Import Pagination Stuff
from django.core.paginator import Paginator, EmptyPage

import calendar
import os
# local imports
from .models import Sermon, Event
from .forms import EventForm, SermonForm


# Create your views here.


def home(request):
    from website.namer import namer
    return render(request, 'website/home.html', {
        "my_stuff": namer,
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

# Events

def calndr(request, year=datetime.now().year, month=datetime.now().strftime('%B'), day=datetime.now().day): # %B = month 
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # create a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    # get current year
    now = datetime.now()
    current_year = now.year

    # Get current Day
    current_day = now.day

    #get current time
    time = now.strftime('%I:%M %p') # %I = standard time, %H = military time... %p = am/pm,

    # Events (Database)
    

    # Query Events Model for Dates
    event_list = Event.objects.filter(
        event_date__year = year,
        event_date__month = month_number,
    )


    
    return render(request, 'website/cal.html', {
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal': cal,
        'current_year': current_year,
        'current_day': current_day,
        'time': time,
        'event_list': event_list,
    })

def event_list(request):

    # Set up Pagination
    p = Paginator(Event.objects.all().order_by('-event_date'), 10)
    page = request.GET.get('page')  
    event_page = p.get_page(page)
    nums = "a" * event_page.paginator.num_pages


    return render(request, 'website/event_list.html', {
        'event_page': event_page,
        'nums': nums,

    })

def add_event(request):
    submitted = False
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add-event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'website/add_event.html', {
        'form': form,
        'submitted': submitted
    })

def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('calendar')

    return render(request, 'website/update_event.html', {
        'event': event,
        'form': form,

    })

def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user.is_authenticated:
        event.delete()
        messages.success(request, ('Event has been deleted.'))
        return redirect('calendar')
    else:
        messages.success(request, ('You are not authorized to access this page.'))
        return redirect('calendar')

# Contact

def contact(request):
    if request.method == "POST":

        message_subject = request.POST['message-subject']
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
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
            'message_name': message_name,
            })

    else:
        return render(request, 'website/contact.html', {

        })
