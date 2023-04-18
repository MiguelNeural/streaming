from django.shortcuts import render

def index(request):
    print(request.session)
    return render(request, 'dashboard/pages/template.html')