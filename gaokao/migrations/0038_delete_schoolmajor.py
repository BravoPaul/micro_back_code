# Generated by Django 2.2.13 on 2020-07-14 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gaokao', '0037_gaokaometarank_gaokaometascoreline_gaokaorecallrank_gaokaorecallscore_schoolmajor_schoolscore'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SchoolMajor',
        ),
    ]