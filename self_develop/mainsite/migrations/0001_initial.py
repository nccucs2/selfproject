# Generated by Django 2.0.5 on 2018-05-17 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_ID', models.IntegerField(default=0)),
                ('Name', models.CharField(max_length=200)),
            ],
        ),
    ]