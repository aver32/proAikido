from django.shortcuts import render


def maps(request):
    return render(request, 'map_screen/maps.html')
