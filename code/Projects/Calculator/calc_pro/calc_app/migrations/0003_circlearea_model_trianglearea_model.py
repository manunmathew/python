# Generated by Django 5.1.3 on 2024-11-13 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc_app', '0002_div_model_multi_model_sub_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='CircleArea_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radius', models.FloatField()),
                ('area', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TriangleArea_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.FloatField()),
                ('height', models.FloatField()),
                ('area', models.FloatField()),
            ],
        ),
    ]
