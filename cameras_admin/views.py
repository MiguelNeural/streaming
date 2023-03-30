from django.shortcuts import render, redirect
import multiprocessing.connection
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from .modules.camera import VideoCamera, gen

# Create your views here.
def cameras(request):
    return render(request, 'cameras_admin/cameras.html')

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


@gzip.gzip_page
def video_feed(request):
    result = request.GET.get('result', '')
    try:
        cam = VideoCamera(str(result))
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass