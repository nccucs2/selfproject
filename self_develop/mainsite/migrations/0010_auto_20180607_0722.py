# Generated by Django 2.0.5 on 2018-06-07 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0009_auto_20180518_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Name',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]
