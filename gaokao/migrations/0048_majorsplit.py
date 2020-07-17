# Generated by Django 2.2.13 on 2020-07-16 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaokao', '0047_delete_majorsplit'),
    ]

    operations = [
        migrations.CreateModel(
            name='MajorSplit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major_id', models.CharField(blank=True, max_length=200, null=True)),
                ('major_name', models.CharField(blank=True, max_length=200, null=True)),
                ('mid', models.CharField(blank=True, max_length=200, null=True)),
                ('mname', models.CharField(blank=True, max_length=200, null=True)),
                ('cid', models.CharField(blank=True, max_length=200, null=True)),
                ('cname', models.CharField(blank=True, max_length=200, null=True)),
                ('sid', models.CharField(blank=True, max_length=200, null=True)),
                ('sname', models.CharField(blank=True, max_length=200, null=True)),
                ('match_type', models.IntegerField(default=0)),
            ],
        ),
    ]