# Generated by Django 3.0.9 on 2020-09-02 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200902_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='title2',
            field=models.CharField(blank=True, help_text='قم بادخال عنوان للرابط الذي تريد وضعه او للصوره التي تريد وضعها', max_length=100, null=True, verbose_name='العنوان'),
        ),
    ]
