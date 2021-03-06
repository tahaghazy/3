# Generated by Django 3.0.9 on 2020-09-02 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20200901_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='url',
            field=models.URLField(blank=True, help_text='قم بادخال الرابط ', null=True, verbose_name='الرابط'),
        ),
        migrations.AlterField(
            model_name='post',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='media', verbose_name='المخطط'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.TextField(blank=True, help_text='قم بادخال الوصف', null=True, verbose_name='الوصف'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='media', verbose_name='المخطط'),
        ),
        migrations.CreateModel(
            name='PostSS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='قم بادخال عنوان المنشور', max_length=100, verbose_name='العنوان')),
                ('content', models.TextField(blank=True, help_text='قم بادخال الوصف', null=True, verbose_name='الوصف')),
                ('files', models.FileField(blank=True, null=True, upload_to='media', verbose_name='الصوره')),
                ('url', models.URLField(blank=True, help_text='قم بادخال الرابط ', null=True, verbose_name='الرابط')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, help_text='يفضل تركه فارغا', null=True, unique=True)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now, help_text='يفضل تركه كما هو', verbose_name='تاريخ المنشور')),
                ('post_update', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True, verbose_name='تفعيل')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='المستخدم')),
            ],
            options={
                'verbose_name': ' سياره ',
                'verbose_name_plural': '  سيارات',
                'ordering': ('-post_date',),
            },
        ),
    ]
