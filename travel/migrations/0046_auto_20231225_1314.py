# Generated by Django 2.2 on 2023-12-25 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0045_auto_20231225_0345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingmodel',
            old_name='b_plan',
            new_name='b_trip',
        ),
    ]