from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class SuperAdmin(models.Model):
    SadminId = models.AutoField(primary_key=True)
    SadminName = models.TextField(max_length= 80)
    SadminUid = models.TextField(max_length=14)
    SadminPass = models.TextField(null=False, max_length=15)

    def __str__(self):
        return self.SadminName