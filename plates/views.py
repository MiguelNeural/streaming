from django.shortcuts import render

def plates(request):
    return render(request, 'plates/plates.html')