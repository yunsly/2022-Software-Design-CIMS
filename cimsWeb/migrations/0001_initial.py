# Generated by Django 4.0 on 2021-12-19 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoronicStatusOfKorea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
                ('coronicCount', models.IntegerField()),
                ('coronicGap', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CoronicStatusOfRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
                ('coronicCount', models.IntegerField()),
                ('coronicGap', models.IntegerField()),
            ],
        ),
    ]
