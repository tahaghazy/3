# Generated by Django 3.0.9 on 2020-08-31 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200831_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='files',
            field=models.FileField(default=False, upload_to=''),
        ),
    ]
