# Generated by Django 2.0.1 on 2018-04-25 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_auto_20180424_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='code_path',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
