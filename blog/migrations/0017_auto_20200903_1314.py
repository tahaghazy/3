# Generated by Django 3.0.9 on 2020-09-03 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20200903_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=False, help_text='قم بادخال العنوان ', max_length=100, verbose_name='العنوان'),
        ),
    ]
