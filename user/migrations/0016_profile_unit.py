# Generated by Django 3.0.9 on 2020-09-16 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_remove_profile_member_of'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member_set', to='user.Unit'),
        ),
    ]
