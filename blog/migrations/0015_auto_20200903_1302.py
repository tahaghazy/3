# Generated by Django 3.0.9 on 2020-09-03 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200903_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='files2',
        ),
        migrations.AddField(
            model_name='posts',
            name='files2',
            field=models.FileField(blank=True, help_text='قم باضافتها اذا كنت تريد وضع صوره بدل العنوان', null=True, upload_to='media', verbose_name='صورة العنوان'),
        ),
    ]