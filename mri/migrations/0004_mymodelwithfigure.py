# Generated by Django 3.2.4 on 2021-11-24 20:21

from django.db import migrations, models
import django_matplotlib.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mri', '0003_auto_20211124_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModelWithFigure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fig', django_matplotlib.fields.MatplotlibFigureField()),
            ],
        ),
    ]
