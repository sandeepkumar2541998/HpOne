# Generated by Django 3.1.4 on 2021-01-27 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SuperBikes', '0004_supercars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carbrands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('img_address', models.CharField(max_length=100)),
            ],
        ),
    ]
