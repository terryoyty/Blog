# Generated by Django 2.2.3 on 2020-04-28 08:48

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191206_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=mdeditor.fields.MDTextField(verbose_name='正文'),
        ),
    ]
