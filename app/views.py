from django.shortcuts import render
from django.http import HttpResponse
from app import forms
from app.models import *


# Create your views here.
def index(request):
    titlee = title.objects.all()[0]
    subcribe_form = forms.subcribe_form()
    if request.method == "POST":
        subcribe_form = forms.subcribe_form(request.POST)
        if subcribe_form.is_valid():
            subcribe_form.save(commit=True)

    diction = {'title':titlee,'subcribe_form':subcribe_form}
    return render(request,'index.html',context=diction)

def about(request):
    return render(request,'about.html')

def contact(request):
    contact_form = forms.contact_form()
    if request.method == "POST":
        contact_form = forms.contact_form(request.POST)
        if contact_form.is_valid():
            contact_form.save(commit=True)
    diction = {'contact_form': contact_form}
    return render(request,'contact.html',context=diction)

def portfolio(request):
    return render(request,'portfolio.html')

def login(request):
    return render(request,'login.html')

