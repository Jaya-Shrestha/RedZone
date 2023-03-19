# Generated by Django 4.1.7 on 2023-03-19 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='redzone',
            name='cause',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='redzone',
            name='title',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='redzone',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
