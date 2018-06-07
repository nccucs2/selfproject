# Generated by Django 2.0.5 on 2018-05-18 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0008_auto_20180518_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Credit',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='course',
            name='Remark',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='studied',
            name='GPA',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='studied',
            name='Score',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
    ]