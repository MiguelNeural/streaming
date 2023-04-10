from django.db import models

class Camera(models.Model):
    camera_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    rtsp = models.TextField()
    peop_c_service = models.BooleanField(default=False, verbose_name='People Count Service')
    face_rec_service = models.BooleanField(default=False, verbose_name='Face Recognition Service')
    vehicles_service = models.BooleanField(default=False, verbose_name='Vehicles Detection Service')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, blank=True)

    class Meta:
        app_label = 'cameras_admin'
        db_table = 'cameras'
        managed = False
    using = 'neuralDB'
    