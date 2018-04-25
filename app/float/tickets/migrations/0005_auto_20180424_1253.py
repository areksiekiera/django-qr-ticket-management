# Generated by Django 2.0.1 on 2018-04-24 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_ticket_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='room_type',
            field=models.CharField(choices=[('T', 'Tank'), ('R', 'Room')], max_length=1),
        ),
    ]