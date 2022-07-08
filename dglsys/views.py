from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import SubmisyonForm, DigitalForm

installed_apps = ['dglsys']

def MainPage(request):
	return render(request, 'one.html')

def Information(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		sex = request.POST['sex']
		country = request.POST['country']
		descr = request.POST['descr']
		data = Submisyon.objects.create(fnam = name, emayl = email, seks = sex, countri = country, descr = descr)
		data.save()
	
	return render (request, 'two.html')

def records(request):
	if request.method == 'POST':
		types = request.POST['types']
		resolu = request.POST['resolu']
		orientat = request.POST['orientat']
		Nart = request.POST['Nart']
		price = request.POST['price']
		currency = request.POST['currency']

		main = request.POST['main']
		second = request.POST['second']
		brand = request.POST['brand']
		model = request.POST['model']
		data = Digitaltype.objects.create(tda = types, reso = resolu, orient = orientat, nameart = Nart, prays = price, curr = currency)
		data1 = Devicedused.objects.create(mayn = main, sekond = second, brando = brand, modelo = currency,)

		data.save()
		data1.save()
	sSubmisyon = Submisyon.objects.all()
	sDigitaltype = Digitaltype.objects.all()
	return render (request, 'table.html', {'Submisyon':sSubmisyon,'Digitaltype':sDigitaltype})


def update(request, id):
	sub = Submisyon.objects.get(id=id)
	form = SubmisyonForm(instance=sub)
	if request.method == 'POST':
		form = SubmisyonForm(request.POST, instance = sub)
		if form.is_valid():
			form.save()
			return redirect('/records')

	return render(request, 'update.html', {'form':form})
		
def delete(request, id):
    a = Submisyon.objects.get(id=id)
    for x in Submisyon.objects.only('id'):
        if a == x:
            x = Submisyon.objects.get(id=id).delete()
            break
    return redirect('/records')

def update1(request, id):
	sub = Digitaltype.objects.get(id=id)
	form = DigitalForm(instance=sub)
	if request.method == 'POST':
		form = DigitalForm(request.POST, instance = sub)
		if form.is_valid():
			form.save()
			return redirect('/records')

	return render(request, 'update1.html', {'form':form})
		
def delete1(request, id):
    a = Digitaltype.objects.get(id=id)
    for x in Digitaltype.objects.only('id'):
        if a == x:
            x = Digitaltype.objects.get(id=id).delete()
            break
    return redirect('/records')





