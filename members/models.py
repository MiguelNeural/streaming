from django.db import models

class Member(models.Model):
    member_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    password = models.TextField()
    role = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, blank=True)

    class Meta:
        app_label = 'members'
        db_table = 'members'
        managed = False