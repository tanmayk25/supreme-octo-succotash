# Generated by Django 2.2.5 on 2022-05-09 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SwingBeatsApp', '0003_auto_20220509_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.IntegerField(blank=True, help_text='Enter your weight in Kilograms'),
        ),
    ]
