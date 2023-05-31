# Generated by Django 4.2.1 on 2023-05-26 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceId', models.CharField(max_length=250)),
                ('cat_name', models.CharField(max_length=250)),
                ('pro_quantity', models.CharField(max_length=250)),
                ('sale', models.CharField(max_length=250)),
                ('cus_name', models.CharField(max_length=250)),
                ('product_name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('method', models.CharField(max_length=250)),
                ('contact', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('cost', models.CharField(max_length=250)),
                ('SKU', models.CharField(max_length=250)),
                ('profit', models.CharField(max_length=250)),
                ('total', models.CharField(max_length=250)),
            ],
        ),
    ]
