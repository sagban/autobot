from django.db import models

# Create your models here.
class Admin(models.Model):
    adminId = models.AutoField(primary_key=True)
    adminName = models.TextField(max_length= 80)
    adminUid = models.TextField(max_length=14)
    adminPass = models.TextField(null=False, max_length=15)

    def __str__(self):
        return self.adminName


class Crime(models.Model):
    offenceId = models.AutoField(primary_key=True)
    offenceName = models.TextField(max_length = 1000)
    offenceName = models.IntegerField(null = True)
    offenceSentence = models.TextField(max_length = 2000, null=True)
    offenceSection = models.TextField(max_length = 1000)

    def __str__(self):
        return self.offenceName



