# Generated by Django 2.2.13 on 2020-07-16 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaokao', '0045_majorsplit'),
    ]

    operations = [
        migrations.AddField(
            model_name='majorsplit',
            name='match_type',
            field=models.IntegerField(default=0),
        ),
    ]