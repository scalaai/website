from django.shortcuts import render


def areas(request):
    return render(request, 'areas/areas.html')
