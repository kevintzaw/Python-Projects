# Generated by Django 3.2.12 on 2022-03-04 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('course_number', models.IntegerField()),
                ('instructor_name', models.CharField(max_length=50)),
                ('duration', models.FloatField()),
            ],
        ),
    ]
