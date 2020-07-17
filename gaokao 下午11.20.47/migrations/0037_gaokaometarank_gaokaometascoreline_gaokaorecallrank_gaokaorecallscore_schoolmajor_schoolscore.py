# Generated by Django 2.2.13 on 2020-07-14 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gaokao', '0036_auto_20200714_0320'),
    ]

    operations = [
        migrations.CreateModel(
            name='GaokaoMetaRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_id', models.CharField(default='', max_length=200)),
                ('province', models.CharField(default='河北', max_length=200)),
                ('academic_year', models.CharField(default='2019', max_length=200)),
                ('wenli', models.CharField(default='1', max_length=200)),
                ('score', models.IntegerField(default=300)),
                ('rank', models.IntegerField(default=200)),
                ('rank_cum', models.IntegerField(default=200)),
            ],
        ),
        migrations.CreateModel(
            name='GaokaoMetaScoreLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_id', models.CharField(default='', max_length=200)),
                ('province', models.CharField(default='河北', max_length=200)),
                ('wenli', models.CharField(default='1', max_length=200)),
                ('batch_name', models.CharField(default='本科第一批', max_length=200)),
                ('academic_year', models.CharField(default='2019', max_length=200)),
                ('school_line', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='GaokaoRecallRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_id', models.CharField(default='', max_length=200)),
                ('province', models.CharField(default='河北', max_length=200)),
                ('wenli', models.CharField(default='1', max_length=200)),
                ('batch_name', models.CharField(default='本科第一批', max_length=200)),
                ('rank', models.IntegerField(default=0)),
                ('school_win', models.TextField(blank=True, null=True)),
                ('school_lose', models.TextField(blank=True, null=True)),
                ('school_predict', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GaokaoRecallScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_id', models.CharField(default='', max_length=200)),
                ('province', models.CharField(default='河北', max_length=200)),
                ('wenli', models.CharField(default='1', max_length=200)),
                ('batch_name', models.CharField(default='本科第一批', max_length=200)),
                ('score', models.IntegerField(default=0)),
                ('school_win', models.TextField(blank=True, null=True)),
                ('school_lose', models.TextField(blank=True, null=True)),
                ('school_predict', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_id', models.CharField(default='', max_length=200)),
                ('academic_year', models.CharField(default='', max_length=200)),
                ('wenli', models.CharField(default='', max_length=200)),
                ('batch', models.CharField(default='', max_length=200)),
                ('batch_name', models.CharField(default='', max_length=200)),
                ('diploma_id', models.CharField(default='', max_length=200)),
                ('admission_count', models.CharField(blank=True, max_length=200, null=True)),
                ('enroll_plan_count', models.CharField(blank=True, max_length=200, null=True)),
                ('max_score', models.CharField(blank=True, max_length=200, null=True)),
                ('max_score_diff', models.CharField(blank=True, max_length=200, null=True)),
                ('max_score_equal', models.CharField(blank=True, max_length=200, null=True)),
                ('max_score_rank', models.CharField(blank=True, max_length=200, null=True)),
                ('min_score', models.CharField(blank=True, max_length=200, null=True)),
                ('min_score_diff', models.CharField(blank=True, max_length=200, null=True)),
                ('min_score_equal', models.CharField(blank=True, max_length=200, null=True)),
                ('min_score_rank', models.CharField(blank=True, max_length=200, null=True)),
                ('avg_score', models.CharField(blank=True, max_length=200, null=True)),
                ('avg_score_diff', models.CharField(blank=True, max_length=200, null=True)),
                ('avg_score_equal', models.CharField(blank=True, max_length=200, null=True)),
                ('avg_score_rank', models.CharField(blank=True, max_length=200, null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaokao.School')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolMajor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_id', models.CharField(default='', max_length=200)),
                ('wenli', models.CharField(default='', max_length=200)),
                ('academic_year', models.CharField(default='', max_length=200)),
                ('batch', models.CharField(default='', max_length=200)),
                ('batch_name', models.CharField(default='', max_length=200)),
                ('diploma_id', models.CharField(default='', max_length=200)),
                ('academic_rule', models.CharField(blank=True, max_length=200, null=True)),
                ('admission_count', models.CharField(blank=True, max_length=200, null=True)),
                ('avg_score', models.CharField(blank=True, max_length=200, null=True)),
                ('avg_score_diff', models.CharField(blank=True, max_length=200, null=True)),
                ('avg_score_rank', models.CharField(blank=True, max_length=200, null=True)),
                ('enroll_major_code', models.CharField(blank=True, max_length=200, null=True)),
                ('enroll_major_id', models.CharField(blank=True, max_length=200, null=True)),
                ('enroll_major_name', models.CharField(blank=True, max_length=200, null=True)),
                ('enroll_plan_count', models.CharField(blank=True, max_length=200, null=True)),
                ('max_score', models.CharField(blank=True, max_length=200, null=True)),
                ('max_score_diff', models.CharField(blank=True, max_length=200, null=True)),
                ('max_score_rank', models.CharField(blank=True, max_length=200, null=True)),
                ('min_score', models.CharField(blank=True, max_length=200, null=True)),
                ('min_score_diff', models.CharField(blank=True, max_length=200, null=True)),
                ('min_score_rank', models.CharField(blank=True, max_length=200, null=True)),
                ('tuition', models.CharField(blank=True, max_length=200, null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaokao.School')),
            ],
        ),
    ]
