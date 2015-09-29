from django.shortcuts import render, HttpResponse
from django.conf import settings


def requestcab(request):
    Lat = float(getattr(settings, "USER_LAT", None))
    Lon = float(getattr(settings, "USER_LON", None))
    print Lat
    print Lon
    #TODO: INSERT OLA API CALL
    return HttpResponse("Cab requested at {0}, {1}!".format(Lat,Lon))
    
def authOla(request):
    #TODO: INSERT OLA AUTH PROCESS
    return HttpResponse("Move along, nothing to look here.")    