# Generated by Django 2.2.13 on 2020-07-16 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaokao', '0049_schoolmajorsplit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schoolmajorsplit',
            old_name='mscore',
            new_name='avg_score_diff',
        ),
        migrations.AddField(
            model_name='schoolmajorsplit',
            name='avg_score_rank',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='schoolmajorsplit',
            name='max_score_diff',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='schoolmajorsplit',
            name='max_score_rank',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='schoolmajorsplit',
            name='min_score_diff',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='schoolmajorsplit',
            name='min_score_rank',
            field=models.IntegerField(default=100),
        ),
    ]
