from django.shortcuts import render

def plates(request):
    context = {
        'headerTitle': 'Registro de placas vehiculares',
        'breadcrumb': [
            {"tag": "Registro de placas", "url": "plates"},
        ],
    }
    return render(request, 'plates/plates.html', context)