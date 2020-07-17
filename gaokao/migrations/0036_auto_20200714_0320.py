# Generated by Django 2.2.13 on 2020-07-14 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gaokao', '0035_gaokaometascoreline'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GaokaoMetaRank',
        ),
        migrations.DeleteModel(
            name='GaokaoMetaScoreLine',
        ),
        migrations.DeleteModel(
            name='GaokaoRecallRank',
        ),
        migrations.DeleteModel(
            name='GaokaoRecallScore',
        ),
        migrations.RemoveField(
            model_name='schoolscore',
            name='school',
        ),
        migrations.DeleteModel(
            name='SchoolMajor',
        ),
        migrations.DeleteModel(
            name='SchoolScore',
        ),
    ]