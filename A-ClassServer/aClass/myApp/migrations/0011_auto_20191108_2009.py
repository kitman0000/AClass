# Generated by Django 2.2.1 on 2019-11-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_auto_20191108_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuploadinfo',
            name='mark',
            field=models.IntegerField(),
        ),
    ]
