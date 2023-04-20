from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.core import serializers
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from .models import Member as Member_mdl
from .modules.forms import Member_form

def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        members = Member_mdl.objects.filter(name=name, deleted__isnull=True)
        if members:
            for member in members:
                if member.login_isValid(name, password):
                    return redirect('dashboard')
        context = {
            'show_alert': 'error',
            'message': 'Nombre de usuario o contraseña incorrectos',
        }
        return render(request, 'members/login.html', context)
    return render(request, 'members/login.html')

def paginator(request, directory):
    p = Paginator(directory, 10)
    page = request.GET.get('page')
    members_list = p.get_page(page)
    pages = range(1, members_list.paginator.num_pages + 1)
    many_pages = [page for page in range(max(members_list.number-3, 1), min(members_list.number+4, members_list.paginator.num_pages+1))]
    return {
        'members_list': members_list,
        'pages': pages,
        'many_pages': many_pages,
    }
    
def members(request):
    members = Member_mdl.objects.filter(deleted__isnull=True)
    context = paginator(request, members)
    if request.method == 'GET':
        context['show_alert'] = request.GET.get('show_alert')
        context['message'] = request.GET.get('message')
    return render(request, 'members/members.html', context)

def create_member(request):
    if request.method == 'POST':
        form = Member_form(request.POST)
        if form.is_valid():
            # Hash the password field
            password = form.cleaned_context.get('password')
            hashed_password = make_password(password)
            form.cleaned_context['password'] = hashed_password
            
            form.save()
            message = "Usuario agregada correctamente"
            show_alert = "success"
            url = reverse('members') + f"?message={message}&show_alert={show_alert}"
            return redirect (url)
        else:
            members = Member_mdl.objects.filter(deleted__isnull=True)
            context = { 'members': members, }
            return render(request, 'members/members.html', context)
    else:
        members = Member_mdl.objects.filter(deleted__isnull=True)
        context = { 'members': members, }
        return render(request, 'members/members.html', context)
    
def edit_member(request, id):
    members = Member_mdl.objects.filter(deleted__isnull=True)
    context = paginator(request, members)
    try:
        memberById = Member_mdl.objects.filter(pk=id, deleted__isnull=True).first()
        memberById_json = serializers.serialize('json', [memberById])
    except:
        message = "Usuario no encontrado en base de datos"
        show_alert = "success"
        url = reverse('members') + f"?message={message}&show_alert={show_alert}"
        return redirect (url)
    
    context['memberById'] = memberById
    context['memberById_json'] = memberById_json
    
    if request.method == 'POST':
        form = Member_form(request.POST)
        if form.is_valid():
            memberById.name = request.POST.get('name')
            memberById.role = request.POST.get('role')
            memberById.save()
            
            message = "Usuario editado correctamente"
            show_alert = "success"
            url = reverse('members') + f"?message={message}&show_alert={show_alert}"
            return redirect (url)
        else:
            message = "Error editando el usuario"
            show_alert = "error"
            url = reverse('members') + f"?message={message}&show_alert={show_alert}"
            return redirect (url)
            
    return render(request, 'members/members.html', context)

def delete_member(request, id):
    members = Member_mdl.objects.filter(deleted__isnull=True)
    context = paginator(request, members)
    try:
        memberById = Member_mdl.objects.filter(pk=id, deleted__isnull=True).first()
        context['memberById'] = memberById
    except:
        return redirect('members')
    
    if request.method == 'POST':
        memberById.deleted = timezone.now()
        memberById.save()
        
        message = "Usuario eliminado correctamente"
        show_alert = "success"
        url = reverse('members') + f"?message={message}&show_alert={show_alert}"
        return redirect (url)
    
    return render(request, 'members/members.html', context)