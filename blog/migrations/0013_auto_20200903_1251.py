# Generated by Django 3.0.9 on 2020-09-03 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200902_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='files',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='الصوره'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, help_text='قم بادخال اسم التصنيف ', max_length=255, null=True, verbose_name='التصنيف'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='قم بادخال العنوان ', max_length=100, verbose_name='العنوان'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title2',
            field=models.CharField(blank=True, help_text='قم بادخال عنوان للرابط الذي تريد وضعه او للصوره التي تريد وضعها', max_length=100, null=True, verbose_name='عنوان الرابط او الصوره'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(help_text='قم بادخال العنوان ', max_length=100, verbose_name='العنوان'),
        ),
        migrations.AlterField(
            model_name='postss',
            name='title',
            field=models.CharField(help_text='قم بادخال العنوان ', max_length=100, verbose_name='العنوان'),
        ),
    ]