# Generated by Django 3.0.5 on 2020-04-25 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]