from django.shortcuts import render, redirect
from carbook_app import models
from carbook_app import forms

# Create your views here.

def add_booking_view(request):
    if request.method == 'POST':
        form = forms.carbooking_data(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_booking_view')
        else:
            print(forms.errors)
    return render(request,'add_booking.html')

def list_booking_view(request):
    booking = models.carbooking.objects.all()
    context = {'booking':booking}
    return render(request,'list_booking.html',context)

def update_booking_view(request,id):
    up = models.carbooking.objects.get(id=id)
    if request.method == 'POST':
        form = forms.carbooking_data(request.POST, instance=up)
        if form.is_valid():
            form.save()
            return redirect('list_booking_view')
        else:
            print(forms.errors)
    context = {'up':up}
    return render(request,'update_booking.html',context)

def delete_booking_view(request,id):
    de = models.carbooking.objects.get(id=id)
    de.delete()
    return redirect('list_booking_view')