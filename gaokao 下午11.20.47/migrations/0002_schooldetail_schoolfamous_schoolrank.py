# Generated by Django 3.0.7 on 2020-06-29 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gaokao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_type_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('rank_year', models.IntegerField(blank=True, null=True)),
                ('rank_idx', models.IntegerField(blank=True, null=True)),
                ('rank_score', models.FloatField(blank=True, null=True)),
                ('rank_type', models.CharField(blank=True, max_length=200, null=True)),
                ('world_rank_idx', models.IntegerField(blank=True, null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaokao.School')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolFamous',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celebrity_name', models.CharField(blank=True, max_length=200, null=True)),
                ('celebrity_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaokao.School')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canteen_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('sch_address', models.CharField(blank=True, max_length=200, null=True)),
                ('sch_fellowship', models.CharField(blank=True, max_length=200, null=True)),
                ('sch_intro', models.CharField(blank=True, max_length=200, null=True)),
                ('sch_scholarship', models.CharField(blank=True, max_length=200, null=True)),
                ('sch_tel_num', models.CharField(blank=True, max_length=200, null=True)),
                ('sch_web_url', models.CharField(blank=True, max_length=200, null=True)),
                ('stu_dorm_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaokao.School')),
            ],
        ),
    ]
