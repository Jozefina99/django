from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.http import HttpResponse
from ticketSales.models import concertModel
from ticketSales.models import locationModel
from ticketSales.models import timeModel
import accounts
from django.urls import reverse

# Create your views here.

def concertListView(request):

	concerts=concertModel.objects.all()

	#return HttpResponse(concerts)
	context={

		"concertlist":concerts,
		"concertcount":concerts.count()
	}
	return render(request,"ticketSales/concertlist.html",context)


def locationListView(request):

	locations=locationModel.objects.all()

	#return HttpResponse(concerts)
	context={

		"locationlist":locations
	}
	return render(request,"ticketSales/locationlist.html",context)

def concertDetailesView(request,concert_id):

	concert=concertModel.objects.get(pk=concert_id)

	context={

		"concertDetailes":concert
	}

	return render(request,"ticketSales/concertDetailes.html",context)

def timeView(request):
	if request.user.is_authenticated and request.user.is_active:

		times=timeModel.objects.all()

		context={

			"timelist":times
		}

		return render(request,"ticketSales/timeList.html",context)
	else:
		#return HttpResponse("اجازه  ورود ندارید")
		return HttpResponseRedirect(reverse(accounts.views.loginView))