import cv2
import threading

class VideoCamera(object):
    def __init__(self, rtsp):
        self.video = cv2.VideoCapture(rtsp)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        try:
            _, jpeg = cv2.imencode('.jpg', self.frame)
        except cv2.error as e:
            print(f"Ya la regaste chavo: {e}")
            self.video = cv2.VideoCapture(0)
            (self.grabbed, self.frame) = self.video.read()
            _, jpeg = cv2.imencode('.jpg', self.frame) #Agregar excepcion en caso de no encontrar webcam|
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')