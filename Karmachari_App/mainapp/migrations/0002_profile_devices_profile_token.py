# Generated by Django 4.1.7 on 2023-05-02 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='devices',
            field=models.ManyToManyField(blank=True, null=True, to='mainapp.device'),
        ),
        migrations.AddField(
            model_name='profile',
            name='token',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
