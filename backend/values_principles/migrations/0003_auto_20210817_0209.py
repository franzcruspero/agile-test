# Generated by Django 3.2.6 on 2021-08-17 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('values_principles', '0002_auto_20210817_0156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='principle',
            name='name',
        ),
        migrations.RemoveField(
            model_name='value',
            name='name',
        ),
        migrations.AddField(
            model_name='principle',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='value',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Title'),
        ),
    ]