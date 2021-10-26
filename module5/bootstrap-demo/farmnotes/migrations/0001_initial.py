# Generated by Django 3.2.7 on 2021-09-18 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=200)),
                ('is_planted', models.BooleanField()),
                ('date_planted', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observation_title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('observation_content', models.CharField(max_length=1000)),
                ('observation_date', models.DateTimeField()),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmnotes.field')),
            ],
        ),
    ]
