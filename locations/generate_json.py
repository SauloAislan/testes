from .models import Location
from .serializers import LocationSerializer
from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.utils import timezone
from  datetime import datetime
from pathlib import Path


class generate_json():


    def for_device(device_id):
        points = Location.objects.all()[:200]
        first_element = Location.objects.first()
        last_element = Location.objects.last()
        dataformat =  datetime.strftime(first_element.time, '%Y-%m-%d')
        return render(request, 'map.html', {'points': points, 'device_id': 11, 'first_element': dataformat, 'last_element': last_element})


def send(request, device_id, lat, lng):
    timezone.activate(pytz.timezone("America/Recife"))
    now = timezone.localtime(timezone.now())
    dataformat = datetime.strftime(now, '%Y-%m-%d')

    p = Location(user_id=1, device_id=device_id, lat=lat, lng=lng, alt='15', time=dataformat)
    p.save()

    a_dict = serializers.serialize("json", Location.objects.all())
    my_file = Path("./movep/locations/static/" + device_id + "_" + str(dataformat) + ".json")
    if my_file.is_file():

        with open(str(my_file), "w") as f:
             f.write(a_dict)
    else:
        with open(str(my_file), "w") as out:
            out.write(a_dict)


    # dados_list = Location.objects.all()
    # for dados in dados_list:
    #     print
    #     dados.lng
    return HttpResponse('ok')

