# Generated by Django 2.2.12 on 2020-05-14 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0008_auto_20200514_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='profile_picture',
            field=models.ImageField(blank=True, default='pp.jpg', upload_to='profile_picture'),
        ),
    ]
