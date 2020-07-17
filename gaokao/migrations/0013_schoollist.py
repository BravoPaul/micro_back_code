# Generated by Django 2.2.13 on 2020-07-04 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gaokao', '0012_delete_schoollist'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(blank=True, max_length=200, null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaokao.School')),
            ],
        ),
    ]