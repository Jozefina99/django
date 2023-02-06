from django.contrib.auth import authenticate,login
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import ticketSales
from django.urls import reverse
# Create your views here.
def  loginView(request):
	#POST
	if request.method=='POST':  
	 	username=request.POST.get('username')
	 	password=request.POST.get('password')
	 	user=authenticate(request,username=username,password=password)

	 	if user is not None:
	 		login(request,user)
	 		return HttpResponseRedirect(reverse(ticketSales.views.timeView))
	 		pass
	 	else:
	 		#do somthing
	 		context={
	 		 	"username":username,
	 		 	"errorMessage":"کاربری  با این مشخصات نبود "
	 		}
	 		return render(request,"accounts/login.html",context)
	 #GET
	else:	
	    return render(request,"accounts/login.html",{})
