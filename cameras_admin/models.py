from django.db import models

class Camera(models.Model):
    name = models.TextField()
    rtsp = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, blank=True)

    class Meta:
        app_label = 'cameras_admin'
        db_table = 'cameras'
        managed = False
    using = 'neuralDB'
