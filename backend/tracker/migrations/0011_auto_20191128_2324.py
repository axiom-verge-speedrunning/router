# Generated by Django 2.2.6 on 2019-11-28 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_itemtracker_lab_coat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemtracker',
            old_name='intertial_pulse',
            new_name='inertial_pulse',
        ),
    ]
