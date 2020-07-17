# Generated by Django 2.2.13 on 2020-07-12 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaokao', '0033_delete_gaokaorecallrank'),
    ]

    operations = [
        migrations.CreateModel(
            name='GaokaoRecallRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(default='河北', max_length=200)),
                ('wenli', models.CharField(default='1', max_length=200)),
                ('batch_name', models.CharField(default='本科第一批', max_length=200)),
                ('rank', models.IntegerField(default=0)),
                ('school_win', models.TextField(blank=True, null=True)),
                ('school_lose', models.TextField(blank=True, null=True)),
                ('school_predict', models.TextField(blank=True, null=True)),
            ],
        ),
    ]