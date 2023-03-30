from django.shortcuts import render, redirect

# Create your views here.
def blank(request):
    return redirect('dashboard')

def index(request):
    return render(request, 'dashboard/pages/template.html')