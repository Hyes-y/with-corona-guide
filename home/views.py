from django.shortcuts import render


def intro(request):
    return render(request, 'home/intro.html')

def stepbystepRecovery(request):
    return render(request, 'home/stepbystepRecovery.html')

def overseasTripInfo(request):
    return render(request, 'home/overseasTripInfo.html')