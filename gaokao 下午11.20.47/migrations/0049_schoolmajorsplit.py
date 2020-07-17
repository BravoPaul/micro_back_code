# Generated by Django 2.2.13 on 2020-07-16 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gaokao', '0048_majorsplit'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolMajorSplit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.CharField(blank=True, max_length=200, null=True)),
                ('mname', models.CharField(blank=True, max_length=200, null=True)),
                ('mscore', models.IntegerField(default=100)),
                ('m_level', models.IntegerField(default=-1)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaokao.School')),
            ],
        ),
    ]
