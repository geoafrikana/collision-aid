from django.shortcuts import render
from .models import Shop, ZipCodes
from django.core.serializers import serialize
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.db.models import Max, Min, Avg
import requests
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    if request.method == "POST":
        zip_code = request.POST.get('zip_code')
        radius = int(request.POST.get('search_radius')) * 1000 # km to metres
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
                            'pre_scan', 'post_scan']
                
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
                ser_fields = fields +['business_name', 'physical_address', 'updated', ]
                serialized_geojson = serialize('geojson',res,
                                geometry_field='geom',
                                fields=ser_fields )
                response['data'] = serialized_geojson
        response['code'] = code
        
        return JsonResponse(response)
    return render(request, "shops/index.html")

def rate_survey(request):
    if request.method == 'POST':
        a = {key:request.POST.get(key) for key in request.POST.keys()}
        address = a.get('physical_address')
        url= f'https://nominatim.openstreetmap.org/search/?q={address}&format=json'
        r = requests.get(url)
        try:
            r = r.json()[0]
        except:
            return JsonResponse({'message': 'The physical location could not be verified, please check.'})
        a['lat'] = float(r.get('lat'))
        a['lon'] = float(r.get('lon'))
        s = Shop(**a)
        try:
            s.clean()
            print(s)
        except ValidationError as e:
            return JsonResponse({'message': 'The physical location could not be verified, please check.'})
        s.save()
        return JsonResponse({'message': 'Shop added successfully'})
    return render(request, 'shops/ratesurvey.html')

def contact(request):
    if request.method == 'POST':
        data = {key:request.POST.get(key) for key in request.POST.keys()}
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [data.get('Email'), ]
        subject = f"From {data['First Name']}"
        message = f'Testing mail {data["Message"]}'
        try:
            send_mail(subject, message, email_from, recipient_list)
            response = {'message': 'Your message has been sent',
                        'status': 'success'}
        except:
            response = {'message': 'Your message could not be sent',
                        'status': 'danger'}

        return JsonResponse(response)
    return render(request, 'shops/contact.html')