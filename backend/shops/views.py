from django.shortcuts import render
from .models import Shop, ZipCodes
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
import json


def index(request):
    if request.method == "POST":
        zip_code = request.POST.get('zip_code')
        radius = int(request.POST.get('search_radius')) * 1609.34 # miles to metres
        z = ZipCodes.objects.get(ZIP=zip_code)
        buf = z.geom.buffer(radius)
        res = Shop.objects.filter(
            geom__intersects=buf
        )
        ser_geojson = serialize('geojson',res,
                         geometry_field='geom',
                        fields=('name',) )
        return HttpResponse(ser_geojson)
    return render(request, "shops/index.html")
