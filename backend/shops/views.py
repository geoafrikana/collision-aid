from django.shortcuts import render
from .models import Shop, ZipCodes
from django.core.serializers import serialize
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.db.models import Max, Min, Avg


def index(request):
    if request.method == "POST":
        zip_code = request.POST.get('zip_code')
        radius = int(request.POST.get('search_radius')) * 1609.34 # miles to metres
        response = {}
        try:
            z = ZipCodes.objects.get(ZIP=zip_code)
        except ObjectDoesNotExist:
             code = 1
        else:
            buf = z.geom.buffer(radius)
            res = Shop.objects.filter(geom__intersects=buf)
            if not res:
                code = 2
            else:
                code = 3
                fields = ['body_sheet_metal','refinish_labour',
                           'frame', 'structural','mechanical',
                            'paint_materials','aluminum_body',
                            'aluminum_structure', 'inside_storage',
                            'pre_scan', 'post_scan'   ]
                
                average = [int(res.aggregate(Avg(field))[f'{field}__avg']) for field in fields]
                highest = [int(res.aggregate(Max(field))[f'{field}__max']) for field in fields]
                lowest = [int(res.aggregate(Min(field))[f'{field}__min']) for field in fields]
                table = {
                    'heading': fields, 
                    'highest': highest,
                    'average': average,
                    'lowest': lowest
                }
                print(table)
                response['table'] = table
                serialized_geojson = serialize('geojson',res,
                                geometry_field='geom',
                                fields=('business_name',) )
                response['data'] = serialized_geojson
        response['code'] = code
        
        return JsonResponse(response)
    return render(request, "shops/index.html")

def rate_survey(request):
    return render(request, 'shops/ratesurvey.html')