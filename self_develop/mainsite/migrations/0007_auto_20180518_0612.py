# Generated by Django 2.0.5 on 2018-05-18 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_studies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Code',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
