from django.shortcuts import render

def plates(request):
    context = {
        'headerTitle': 'Registro de placas vehiculares'
    }
    return render(request, 'plates/plates.html', context)