# Generated by Django 3.0.9 on 2020-09-12 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0017_report_taker'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='date_last_progress',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='progress',
            field=models.IntegerField(blank=True, choices=[(1, 'Task Taken'), (2, 'Field Checking'), (3, 'Approved'), (4, 'Not Approved'), (5, 'Responsing'), (6, 'Resolved'), (7, 'Postponed'), (8, 'Failed')], null=True),
        ),
    ]
