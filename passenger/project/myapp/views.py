from django.shortcuts import render,HttpResponseRedirect
from .models import *
from .forms import *
# Create your views here.
#add & display
def add_show(request):
    if request.method == "POST":
        psngr = passenger.objects.all()
        fm = Passengerreg(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            age = fm.cleaned_data['age']
            gender = fm.cleaned_data['gender']
            boarding = fm.cleaned_data['boarding']
            destination = fm.cleaned_data['destination']
            reg = passenger(name=name, age=age, gender=gender, boarding=boarding, destination=destination)
            reg.save()
            fm = Passengerreg()
    else:
        fm = Passengerreg()
        psngr = passenger.objects.all()
    return render(request, 'addshow.html',{'fm':fm,'ps':psngr})

#delete
def delete_data(request,id):
    if request.method == 'POST':
        pi=passenger.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

#edit
def edit_data(request,id):
    if request.method == 'POST':
        pi = passenger.objects.get(pk=id)
        fm = Passengerreg(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = passenger.objects.get(pk=id)
        fm = Passengerreg(instance=pi)
    return render(request, 'update.html', {'form':fm})










