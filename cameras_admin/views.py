from django.shortcuts import render, redirect
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from django.urls import reverse
from django.core import serializers
from django.core.paginator import Paginator
from django.utils import timezone
from .modules.camera import VideoCamera, gen
from .modules.forms import CreateCamera_form
from .models import Camera

# Create your views here.
def paginator(request, directory):
    p = Paginator(directory, 10)
    page = request.GET.get('page')
    cameras_list = p.get_page(page)
    pages = range(1, cameras_list.paginator.num_pages + 1)
    many_pages = [page for page in range(max(cameras_list.number-3, 1), min(cameras_list.number+4, cameras_list.paginator.num_pages+1))]
    return {
        'cameras_list': cameras_list,
        'pages': pages,
        'many_pages': many_pages,
    }

def cameras(request):
    cameras = Camera.objects.filter(deleted__isnull=True)
    data = paginator(request, cameras)
    data['form'] = CreateCamera_form()
    if request.method == 'GET':
        data["show_alert"] = request.GET.get('show_alert', '')
        data["message"] = request.GET.get('message', '')
        
    return render(request, 'cameras_admin/cameras.html', data)
    
def create_camera(request):
    if request.method == 'POST':
        form = CreateCamera_form(request.POST)
        if form.is_valid():
            form.save()
            cameras = Camera.objects.filter(deleted__isnull=True)
            message = "Cámara agregada correctamente"
            show_alert = "success"
            url = reverse('cameras') + f"?message={message}&show_alert={show_alert}"
            return redirect (url)
        else:
            cameras = Camera.objects.filter(deleted__isnull=True)
            data = {
                'form': form,
                'cameras': cameras,
            }
            return render(request, 'cameras_admin/cameras.html', data)
    else:
        form = CreateCamera_form()
        cameras = Camera.objects.filter(deleted__isnull=True)
        data = {
            'form': form,
            'cameras': cameras,
        }
        return render(request, 'cameras_admin/cameras.html', data)
    
def edit_camera(request, id):
    cameras = Camera.objects.filter(deleted__isnull=True)
    data = paginator(request, cameras)
    try:
        cameraById = Camera.objects.filter(pk=id, deleted__isnull=True).first()
        cameraById_json = serializers.serialize('json', [cameraById])
    except:
        return redirect('cameras')
    
    data['cameraById'] = cameraById
    data['cameraById_json'] = cameraById_json
    
    if request.method == 'POST':
        form = CreateCamera_form(request.POST)
        if form.is_valid():
            cameraById.name = request.POST.get('name')
            cameraById.rtsp = request.POST.get('rtsp')
            if(request.POST.get("peop_c_service")):
                cameraById.peop_c_service = True
            else:
                cameraById.peop_c_service = False
            if(request.POST.get("face_rec_service")):
                cameraById.face_rec_service = True
            else:
                cameraById.face_rec_service = False
            if(request.POST.get("vehicles_service")):
                cameraById.vehicles_service = True
            else:
                cameraById.vehicles_service = False
            cameraById.save()
            
            message = "Cámara editada correctamente"
            show_alert = "success"
            url = reverse('cameras') + f"?message={message}&show_alert={show_alert}"
            return redirect (url)
    
    return render(request, 'cameras_admin/cameras.html', data)

def delete_camera(request, id):
    cameras = Camera.objects.filter(deleted__isnull=True)
    data = paginator(request, cameras)
    try:
        cameraById = Camera.objects.filter(pk=id, deleted__isnull=True).first()
    except:
        return redirect('cameras')
    
    data['cameraById'] = cameraById
    
    if request.method == 'POST':
        cameraById.deleted = timezone.now()
        cameraById.save()
        
        message = "Cámara eliminada correctamente"
        show_alert = "success"
        url = reverse('cameras') + f"?message={message}&show_alert={show_alert}"
        return redirect (url)
    
    return render(request, 'cameras_admin/cameras.html', data)

def rtsp_camera(request, id):
    #address = ('192.168.15.103', 6000)
    #conn = multiprocessing.connection.Client(address, authkey=b'secret password')
    #data = 'rtsp://root:Aegis4040@192.168.5.35/live.sdp'
    #conn.send(data)
    #timeout = 15  # set a timeout of seconds
    #while True:
    #    if conn.poll(timeout):
    #        result = conn.recv()
    #        break
    #    else:
    #        result = 'No response from server.'
    #        break
    try:
        cameraById = Camera.objects.filter(pk=id, deleted__isnull=True).first()
    except:
        return redirect('cameras')
    data = {
        'camera_name': cameraById.name,
        'rtsp': cameraById.rtsp,
    }
    return render(request, 'cameras_admin/rtsp.html', data)

# GENERAR VIDEO POR RTSP
@gzip.gzip_page
def video_feed(request):
    rtsp = request.GET.get('rtsp', '')
    try:
        cam = VideoCamera(str(rtsp))
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except Exception as e:
        print(f"\nError \n'{e}'\n en 'video_feed'\n")