# Generated by Django 2.2.1 on 2019-11-08 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_merge_20191108_1957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homeworkbymonth',
            old_name='teacherName',
            new_name='teacher',
        ),
        migrations.RemoveField(
            model_name='teacherlogin',
            name='teacherName',
        ),
        migrations.AddField(
            model_name='homeworkdetail',
            name='timespan',
            field=models.TextField(default=0, verbose_name=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentuploadinfo',
            name='status',
            field=models.BooleanField(),
        ),
    ]