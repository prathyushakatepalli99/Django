from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .models import Appointment ,Medicine ,Pay
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
#from django.views.decorators.csrf import csrf_protect
#from .models import *
from .forms import CreateUserForm,AppointmentForm,MedicineForm,PayForm
# Create your views here.
def homePage(request):
    return render(request,'home.html')

#@csrf_protect
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('new')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('new')
			
		context = {'form': form}
		return render(request, 'signup.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('new')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				# request.session['appointment_name'] = Appointment.name
				# request.session['email'] = Appointment.email
				return redirect('new')
			else:
				messages.info(request, 'Username OR password is incorrect')
    
		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
  logout(request)
  return redirect('login') 

def contactPage(request):
    return render(request,'contact.html')

def aboutPage(request):
    return render(request,'about.html')	

def midPage(request):
    return render(request,'mid.html')

def newPage(request):
    return render(request,'new.html')		
    
@login_required(login_url = 'login')
def appointmentPage(request):
	#form = AppointmentForm()
	#if request.method == 'POST':
	form = AppointmentForm(request.POST or None)
	if form.is_valid():
		form.save()
		#appoinment = form.cleaned_data.get('email')
		#messages.success(request, 'Account was created for ' + appoinment)
		return redirect('pay')
	context = {'form': form}
	return render(request,'appointment.html',context)

@login_required(login_url = 'login')
def medicinePage(request):
	#form = MedicineForm()
	#if request.method == 'POST':
	form = MedicineForm(request.POST)
	if form.is_valid():
		form.save()
		# = form.cleaned_data.get('email')
		#messages.success(request, 'Account was created for ' + medicine
		return redirect('Successful')
	context = {'form': form}
	return render(request,'medicine.html',context)

@login_required(login_url = 'login')
def payPage(request):
	form = PayForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('success')
	context = {'form': form}
	return render(request,'pay.html',context)



@login_required(login_url = 'login')
def servicePage(request):
 	context = {}
 	return render(request,'service.html',context)

@login_required(login_url = 'login')
def DoctorsPage(request):
 	context = {}
 	return render(request,'doctors.html',context)	


@login_required(login_url = 'login')
def SuccessfulPage(request):
    return render(request,'Successful.html')

@login_required(login_url = 'login')
def successPage(request):
    return render(request,'Success.html')		
	



