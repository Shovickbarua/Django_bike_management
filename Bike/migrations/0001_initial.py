# Generated by Django 4.2.1 on 2023-05-26 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=250)),
                ('bike_name', models.CharField(max_length=250)),
                ('bquantity', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('bcost', models.CharField(max_length=250)),
                ('color', models.CharField(max_length=250)),
                ('engine_no', models.CharField(max_length=250)),
                ('chas_no', models.CharField(max_length=250)),
                ('m_veh', models.CharField(max_length=250)),
                ('manu', models.CharField(max_length=250)),
                ('cc', models.CharField(max_length=250)),
                ('seat_cap', models.CharField(max_length=250)),
                ('brake', models.CharField(max_length=250)),
                ('ftyre', models.CharField(max_length=250)),
                ('rtyre', models.CharField(max_length=250)),
                ('weight', models.CharField(max_length=250)),
                ('bike_image', models.ImageField(null=True, upload_to='images')),
            ],
        ),
    ]
