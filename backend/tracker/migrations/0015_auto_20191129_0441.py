# Generated by Django 2.2.6 on 2019-11-29 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0014_itemtracker_heat_seeker'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtracker',
            name='range_nodes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='itemtracker',
            name='size_nodes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
