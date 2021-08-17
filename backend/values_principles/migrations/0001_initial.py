# Generated by Django 3.2.6 on 2021-08-17 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Principle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Principle',
                'verbose_name_plural': 'Principles',
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Value',
                'verbose_name_plural': 'Values',
            },
        ),
    ]
