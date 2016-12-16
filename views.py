from django.shortcuts import render
#from django.conf.urls import url
#from django.http import HttpResponse
from django.views.generic import View
from Lab5.data import hotels, hotels_dict

class HotelsView(View):
    def get(self, request):
        return render(request, 'main_page.html', {'hotels': hotels})

class HotelView(View):
    def get(self, request, id):
        hotel = hotels.get(int(id))
        return render(request, 'hotel.html', {'hotel': hotel})