from django.db import models

class Member(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('technician', 'Técnico'),
        ('operator', 'Operador'),
    )
    
    member_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    password = models.TextField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, blank=True)

    def login_isValid(self, name, password):
        if name == self.name and password == self.password:
            return True
        else:
            return False

    class Meta:
        app_label = 'members'
        db_table = 'members'
        managed = False