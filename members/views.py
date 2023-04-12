from django.shortcuts import render

def login(request):
    return render(request, 'members/login.html')

def members(request):
    return render(request, 'members/members.html')