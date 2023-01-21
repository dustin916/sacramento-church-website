from django.shortcuts import render
import calendar
from calendar import HTMLCalendar

# Create your views here.

def home(request):
    from website.namer import namer
    return render(request, 'home.html', {"my_stuff": namer})

def sermons(request):
    return render(request, 'sermons.html', {})

def calendar(request, year, month):
    return render(request, 'calendar.html', {
        'year': year,
        'month': month,
    })

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})