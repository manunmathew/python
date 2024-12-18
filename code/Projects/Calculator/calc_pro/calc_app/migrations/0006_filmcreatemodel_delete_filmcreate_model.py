# Generated by Django 5.1.3 on 2024-11-16 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc_app', '0005_rename_name_filmcreate_model_films_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmCreateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('films_name', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('director', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='FilmCreate_model',
        ),
    ]
