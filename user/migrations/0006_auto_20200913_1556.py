# Generated by Django 3.0.9 on 2020-09-13 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200913_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='superior',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinate_set', to='user.Unit'),
        ),
    ]
