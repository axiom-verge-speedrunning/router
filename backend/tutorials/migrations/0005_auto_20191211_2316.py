# Generated by Django 2.2.8 on 2019-12-11 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0004_auto_20191211_0114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tutorial',
            options={'ordering': ('title',)},
        ),
    ]
