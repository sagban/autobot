# Generated by Django 2.0.3 on 2018-03-30 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('userName', models.TextField(max_length=80)),
                ('userUid', models.TextField(max_length=14)),
                ('userPass', models.TextField(max_length=15)),
                ('userDob', models.DateField()),
                ('userGender', models.TextField(max_length=6)),
                ('userMail', models.EmailField(max_length=254)),
                ('userAddress', models.TextField(max_length=1000)),
                ('userLicense', models.TextField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='userRegister',
            fields=[
                ('regId', models.AutoField(primary_key=True, serialize=False)),
                ('regLicense', models.TextField(max_length=15)),
                ('regUid', models.TextField(max_length=12)),
                ('regCell', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='userVehicleOwnership',
            fields=[
                ('userVehicleId', models.AutoField(primary_key=True, serialize=False)),
                ('vehicleNumber', models.TextField(max_length=10)),
                ('regDate', models.DateField()),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('vehicleId', models.AutoField(primary_key=True, serialize=False)),
                ('makerModel', models.TextField(max_length=100)),
                ('makerClass', models.TextField(max_length=100)),
                ('fuelType', models.TextField(max_length=100)),
                ('chassisNumber', models.TextField(max_length=100)),
                ('engineNumber', models.TextField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='uservehicleownership',
            name='vehicleId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.vehicle'),
        ),
        migrations.AddField(
            model_name='user',
            name='userCell',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.userRegister'),
        ),
    ]
