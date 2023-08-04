
from django.http import HttpResponse
from django.shortcuts import render
from . models import Department,Doctor
from . forms import BookingForm 
def index(request):
    return render(request,"index.html")
def department(request):
    nafla=Department.objects.all()
    return render(request,"department.html",{'nafla':nafla})
def docter(request):
    anu=Doctor.objects.all()
    return render(request,"docter.html",{'anu':anu})
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Thank You</h1>')
    form = BookingForm()
    return render(request,'booking.html',{'form':form})