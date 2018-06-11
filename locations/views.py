from .models import Location
from .serializers import LocationSerializer
from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
#from .generate_json import generatejson
import pytz
from django.utils import timezone
from  datetime import datetime
from pathlib import Path
from django.http import JsonResponse

class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer

# selecionar por usuarios
    def get_queryset(self):
        user = self.request.user
        return Location.objects.filter(user=user)


def map_view(request):
    # points = Location.objects.filter(user=request.user)
    points = Location.objects.all()
    device_status = points.filter(status='ON')
    device_id = device_status.filter(device_id=12)
    first_element = device_id.first()
    last_element = Location.objects.last()
    dataformat = datetime.strftime(last_element.time, '%Y-%m-%d')
    return render(request, 'map.html', {'points': points, 'device_id': device_id, 'log': device_status, 'ultimo': first_element,
                                        'first_element': dataformat, 'last_element': last_element})


def locations_data(request):
    # username = request.GET.get('username', None)
    points = Location.objects.all()
    device_status = points.filter(status='ON')
    device_id = device_status.filter(device_id=12)
    data = serializers.serialize('json', device_status)
    return HttpResponse(data, content_type="application/json")


def send(request, device_id, lat, lng):
    timezone.activate(pytz.timezone("America/Recife"))
    now = timezone.localtime(timezone.now())
    dataformat = datetime.strftime(now, '%Y-%m-%d')

    p = Location(user_id=1, device_id=device_id, lat=lat, lng=lng, alt='15', time=dataformat)
    p.save()

    a_dict = serializers.serialize("json", Location.objects.all())
    my_file = Path("file.json")
    if my_file.is_file():

        with open(str(my_file), "w") as f:
             f.write(a_dict)
    else:
        with open(str(my_file), "w") as out:
            out.write(a_dict)

    #test = generatejson.for_device(device_id)

    # dados_list = Location.objects.all()
    # for dados in dados_list:
    #     print
    #     dados.lng
    return HttpResponse('ok')