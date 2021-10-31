from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contactdata = contact(name=name, email=email, subject=subject, message=message)
        contactdata.save()
    return render(request,'contact.html')

def portfolio(request):
    return render(request,'portfolio.html')

