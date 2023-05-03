from django.shortcuts import render

def index(request):
    print(request.session)
    context = {
        'headerTitle': "Tablero de control",
        'breadcrumb': [
            {"tag": "Tablero", "url": "dashboard"},
        ],
    }
    return render(request, 'dashboard/pages/template.html', context)