# Generated by Django 4.2.7 on 2023-11-26 22:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('condition', models.CharField(choices=[('Used', 'Used'), (' New', 'New')], default='Used', max_length=50)),
                ('product_type', models.CharField(choices=[('Bike', 'Bike'), ('Parts', 'Parts'), ('Models', 'Models'), ('Other', 'Other')], default='Bike', max_length=50)),
                ('sale_type', models.CharField(choices=[('Available  for pickup', 'Pick Up'), ('Available to ship', 'Ship')], default='Available to ship', max_length=50)),
                ('price', models.FloatField()),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('zipcode', models.CharField(max_length=25)),
                ('main_photo', models.ImageField(upload_to='')),
                ('photo_1', models.ImageField(upload_to='')),
                ('photo_2', models.ImageField(blank=True, upload_to='')),
                ('list_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('contact_email', models.CharField(max_length=50)),
            ],
        ),
    ]