# Generated by Django 2.2.13 on 2020-07-17 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gaokao', '0063_delete_schoolmajorsplit'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolMajorSplit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.CharField(blank=True, max_length=200, null=True)),
                ('mname', models.CharField(blank=True, max_length=200, null=True)),
                ('province_id', models.CharField(default='13', max_length=200)),
                ('wenli', models.CharField(default='1', max_length=200)),
                ('avg_score_diff_mean', models.IntegerField(default=100)),
                ('avg_score_rank_mean', models.IntegerField(default=100)),
                ('min_score_diff_mean', models.IntegerField(default=100)),
                ('min_score_rank_mean', models.IntegerField(default=100)),
                ('max_score_diff_mean', models.IntegerField(default=100)),
                ('max_score_rank_mean', models.IntegerField(default=100)),
                ('avg_score_diff_std', models.IntegerField(default=100)),
                ('avg_score_rank_std', models.IntegerField(default=100)),
                ('min_score_diff_std', models.IntegerField(default=100)),
                ('min_score_rank_std', models.IntegerField(default=100)),
                ('max_score_diff_std', models.IntegerField(default=100)),
                ('max_score_rank_std', models.IntegerField(default=100)),
                ('avg_score_diff_trend', models.IntegerField(default=100)),
                ('avg_score_rank_trend', models.IntegerField(default=100)),
                ('min_score_diff_trend', models.IntegerField(default=100)),
                ('min_score_rank_trend', models.IntegerField(default=100)),
                ('max_score_diff_trend', models.IntegerField(default=100)),
                ('max_score_rank_trend', models.IntegerField(default=100)),
                ('m_level', models.IntegerField(default=-1)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaokao.School')),
            ],
        ),
    ]
