from django.db import models

# Create your models here.

class userRegister(models.Model):
    regId = models.AutoField(primary_key=True)
    regLicense = models.TextField(max_length=15)
    regUid = models.TextField(max_length=12)
    regCell = models.TextField(max_length=10)

    def __str__(self):
        return self.regLicense


class user(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.TextField(max_length= 80)
    userUid = models.TextField(max_length=14)
    userPass = models.TextField(null=False, max_length=15)
    userDob = models.DateField()
    userGender = models.TextField(max_length=6)
    userMail = models.EmailField()
    userAddress = models.TextField(max_length=1000)
    userLicense = models.TextField(max_length=15)
    userCell = models.ForeignKey(userRegister, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.userName

class vehicle(models.Model):
    vehicleId = models.AutoField(primary_key=True)
    #makerModel = models.TextField(max_length=100)
    makerClass = models.TextField(max_length=100)
    fuelType = models.TextField(max_length=100)
    chassisNumber = models.TextField(max_length=100)
    engineNumber = models.TextField(max_length=100)

    def __str__(self):
        return self.makerClass


class userVehicleOwnership(models.Model):
    userVehicleId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(user, null=False, on_delete=models.CASCADE)
    vehicleId = models.ForeignKey(vehicle, null=False, on_delete=models.CASCADE)
    vehicleNumber = models.TextField(max_length=10)
    regDate = models.DateField()

    def __str__(self):
        return self.vehicleNumber