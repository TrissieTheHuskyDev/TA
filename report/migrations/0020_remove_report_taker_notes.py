# Generated by Django 3.0.9 on 2020-09-13 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0019_report_taker_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='taker_notes',
        ),
    ]
