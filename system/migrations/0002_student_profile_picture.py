# Generated by Django 2.2.12 on 2020-05-06 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='image/profile_picture'),
        ),
    ]
