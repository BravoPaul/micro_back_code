# Generated by Django 2.2.13 on 2020-07-19 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaokao', '0082_modelruleresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelruleresult',
            name='type',
            field=models.IntegerField(default=1),
        ),
    ]