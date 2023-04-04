from django.shortcuts import render, redirect
import multiprocessing.connection
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from .modules.camera import VideoCamera, gen
from .modules.forms import CreateCamera_form
from .models import Camera

# Create your views here.
def cameras(request):
    cameras = Camera.objects.filter(deleted__isnull=True)
    data = {
        'form': CreateCamera_form(),
        'cameras': cameras
    }
    return render(request, 'cameras_admin/cameras.html', data)

def send_message(request):
    address = ('192.168.15.103', 6000)
    conn = multiprocessing.connection.Client(address, authkey=b'secret password')
    data = 'rtsp://root:Aegis4040@192.168.5.35/live.sdp'
    conn.send(data)
    timeout = 15  # set a timeout of 5 seconds
    while True:
        if conn.poll(timeout):
            result = conn.recv()
            break
        else:
            result = 'No response from server.'
            break
    context = {'result': result}
    return render(request, 'cameras_admin/cameras.html', context)

# GENERAR VIDEO POR RTSP
@gzip.gzip_page
def video_feed(request):
    result = request.GET.get('result', '')
    try:
        cam = VideoCamera(str(result))
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass
    
def create_camera(request):
    if request.method == 'POST':
        form = CreateCamera_form(request.POST)
        if form.is_valid():
            form.save()
            cameras = Camera.objects.filter(deleted__isnull=True)
            data = {
                'show_alert': "success",
                'message': "Cámara agregada correctamente",
                'cameras': cameras
            }
            return render(request, 'cameras_admin/cameras.html', data)
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

def delete_camera(request):
    cameras = Camera.objects.filter(deleted__isnull=True)
    data = {
        'cameras': cameras
    }
    return render(request, 'cameras_admin/cameras.html', data)