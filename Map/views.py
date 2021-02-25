from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.http import JsonResponse
from allauth.account.forms import LoginForm, SignupForm
from .models import Place, Request
import json

# Create your views here.
class Home(View):
    def get(self, request):
        context = {
            'places': Place.objects.all(),
            'user': request.user
        }
        return render(request, "Map/home.html", context)

    def post(self, request):
        name = request.POST['place']
        lat = request.POST['lat']
        lng = request.POST['lng']

        if (lat != None and lng != None and lat != '' and lng != ''):
            Place.objects.create(user=request.user, name = name,latitude = lat, longitude = lng)
        return redirect('home')

class Places(View):
    def post(self, request):
        return JsonResponse(list(Place.objects.all().values()), safe=False)

def landing(request):
    allauth_signup = SignupForm(request.POST or None)
    context = {
        'form': allauth_signup,
        'user': request.user
    }
    return render(request, 'Map/landing.html', context)

class Opportunity(View):
    def post(self, request):
        request.user.first_name = request.POST['first_name']
        request.user.last_name = request.POST['last_name']
        
        category = request.POST['category']
        description = request.POST['description']
        lat = request.POST['lat']
        lng = request.POST['lng']
        name = request.POST['place']
        Place.objects.create(user=request.user, category=category, description=description, latitude=lat, longitude=lng, name=name)

        return redirect('thankyou')

class MakeRequest(View):
    def get(self, request):
        id = request.GET['place']
        try:
            place = Place.objects.get(id = id)
            context = {
                'place': place
            }
        except:
            context = {
                'error': 'Sorry, this request could not be processed.'
            }
        return render(request, "Map/request.html", context)

    def post(self, request):
        description = request.POST['description']
        place = Place.objects.get(id=request.POST['place'])

        Request.objects.create(user=request.user, description=description, place=place)
        return redirect("thankyou")

def thankyou(request):
    return render(request, "Map/thankyou.html")