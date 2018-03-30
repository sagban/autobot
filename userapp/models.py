from django.db import models

# Create your models here.


class User(models.Model):
    userID = models.AutoField(primary_key=True)
    userName = models.TextField(max_length= 80)
    userUID = models.TextField(max_length=14)
    userPass = models.TextField(null=False, max_length=15)
    userDOB = models.DateField()
    userGender = models.TextField(max_length=6)
    userMail = models.EmailField()
    userAddress = models.TextField(max_length=1000)
    userLicense = models.TextField(max_length=15)
    userCell = models.TextField(max_length=10)

    def __str__(self):
        return self.userUID


class Vehicles(models.Model):
    vehicleID = models.AutoField(primary_key=True)
    engineNumber = models.TextField(max_length=17)
    chassisNumber = models.TextField(max_length=17)
    fuelType = models.TextField(max_length=20)
    makerModel = models.TextField(max_length=20)
    makerClass = models.TextField(max_length=20)
    regDate = models.DateField()
    regAuth = models.TextField(max_length=20)

    def __str__(self):
        return self.vehicleID


class UserVehicleOwnership(models.Model):
    UserVehicleID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    vehicleID = models.ForeignKey(Vehicles, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.UserVehicleID