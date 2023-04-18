from django.shortcuts import render

def index(request):
    return render(request, 'dashboard/pages/template.html')