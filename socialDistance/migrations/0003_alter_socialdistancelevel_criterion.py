# Generated by Django 4.0 on 2021-12-20 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialDistance', '0002_alter_socialdistancelevel_criterion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialdistancelevel',
            name='criterion',
            field=models.CharField(max_length=1000),
        ),
    ]
