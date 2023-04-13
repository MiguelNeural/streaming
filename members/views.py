from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Member as Member_mdl
from .modules.forms import Member_form

def login(request):
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
    data = paginator(request, members)
    if request.method == 'GET':
        data['show_alert'] = request.GET.get('show_alert')
        data['message'] = request.GET.get('message')
    return render(request, 'members/members.html', data)

def create_member(request):
    if request.method == 'POST':
        form = Member_form(request.POST)
        if form.is_valid():
            form.save()
            message = "Usuario agregada correctamente"
            show_alert = "success"
            url = reverse('members') + f"?message={message}&show_alert={show_alert}"
            return redirect (url)
        else:
            members = Member_mdl.objects.filter(deleted__isnull=True)
            data = { 'members': members, }
            return render(request, 'members/members.html', data)
    else:
        members = Member_mdl.objects.filter(deleted__isnull=True)
        data = { 'members': members, }
        return render(request, 'members/members.html', data)