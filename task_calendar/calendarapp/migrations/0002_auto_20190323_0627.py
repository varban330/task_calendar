# Generated by Django 2.1.7 on 2019-03-23 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=7)),
                ('task1', models.CharField(max_length=17)),
                ('task2', models.CharField(max_length=17)),
                ('task3', models.CharField(max_length=17)),
                ('task4', models.CharField(max_length=17)),
                ('task5', models.CharField(max_length=17)),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='DateModel',
        ),
    ]
