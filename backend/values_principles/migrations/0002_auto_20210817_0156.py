# Generated by Django 3.2.6 on 2021-08-17 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('values_principles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principle',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='value',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]