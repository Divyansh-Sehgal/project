# Generated by Django 3.1.1 on 2020-09-15 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0004_auto_20200915_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default='Not Available', max_length=200),
        ),
    ]
