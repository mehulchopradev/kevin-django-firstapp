# Generated by Django 3.0.5 on 2020-05-03 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0007_book_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profilepicpath',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateField(default=datetime.date(2020, 5, 3), null=True),
        ),
    ]