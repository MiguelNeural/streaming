import multiprocessing
import cv2
import threading
import ctypes

class VideoCamera(object):
    tensorflow = ctypes.WinDLL("lib/tensorflow.dll")
    def __init__(self, rtsp):
        # rtsp://root:Aegis4040@192.168.15.103:8554:8554/frstream
        # rtsp://root:Aegis4040@192.168.15.103:8554/mystream
        # pasillo: rtsp://root:Aegis4040@192.168.5.35/live.sdp
        # mantenimiento: rtsp://neural:Aegis4040@192.168.5.46/live.sdp
        # calle: rtsp://neural:Aegis4040@192.168.5.39/live.sdp
        
        # Envíar rtsp al doctor Gehova:
        # address = ('192.168.15.103', 6000)
        # conn = multiprocessing.connection.Client(address, authkey=b'secret password')
        # data = rtsp
        # conn.send(data)
        # timeout = 15  # set a timeout of seconds
        # result = ""
        # while True:
        #    if conn.poll(timeout):
        #        result = conn.recv()
        #    else:
        #        result = 'No response from server.'
        #        break
        
        rtsp = 'rtsp://neural:Aegis4040@192.168.5.46/live.sdp'
        self.video = cv2.VideoCapture(rtsp)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        print("===============================\nObject VideoCamera has been deleted\n===============================")
        self.video.release()

    def get_frame(self):
        try:
            _, jpeg = cv2.imencode('.jpg', self.frame)
        except cv2.error as e:
            print(f"Ya la regaste chavo: {e}")
            self.video = cv2.VideoCapture(0)
            (self.grabbed, self.frame) = self.video.read()
            _, jpeg = cv2.imencode('.jpg', self.frame)
            #Agregar excepcion en caso de no encontrar webcam
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')