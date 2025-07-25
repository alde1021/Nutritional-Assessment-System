# Generated by Django 5.2 on 2025-06-11 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('permalink', models.CharField(max_length=12, unique=True)),
                ('update_date', models.DateTimeField(verbose_name='Last Updated')),
                ('bodytext', models.TextField(blank=True, verbose_name='Page Content')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_no', models.IntegerField()),
                ('last', models.CharField(max_length=25)),
                ('first', models.CharField(max_length=25)),
                ('middle', models.CharField(max_length=25)),
                ('age', models.CharField(max_length=25)),
                ('birthday', models.DateField()),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('gender', models.CharField(max_length=25)),
            ],
        ),
    ]
