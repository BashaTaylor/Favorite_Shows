# Generated by Django 2.2 on 2021-08-04 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_validated_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateTimeField(),
        ),
    ]
