# Generated by Django 3.2.9 on 2021-12-20 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialDistanceLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=1000)),
                ('criterion', models.CharField(max_length=1000)),
                ('privateMeetingRule', models.CharField(max_length=1000)),
                ('festivalRule', models.CharField(max_length=1000)),
                ('rallyRule', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='SocialDistanceLevelOfRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
                ('term', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Do',
            fields=[
                ('socialdistancelevelofregion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='socialDistance.socialdistancelevelofregion')),
            ],
            bases=('socialDistance.socialdistancelevelofregion',),
        ),
        migrations.CreateModel(
            name='Gun',
            fields=[
                ('socialdistancelevelofregion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='socialDistance.socialdistancelevelofregion')),
            ],
            bases=('socialDistance.socialdistancelevelofregion',),
        ),
        migrations.CreateModel(
            name='MetroCity',
            fields=[
                ('socialdistancelevelofregion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='socialDistance.socialdistancelevelofregion')),
            ],
            bases=('socialDistance.socialdistancelevelofregion',),
        ),
        migrations.CreateModel(
            name='SelfGoverningDo',
            fields=[
                ('socialdistancelevelofregion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='socialDistance.socialdistancelevelofregion')),
            ],
            bases=('socialDistance.socialdistancelevelofregion',),
        ),
        migrations.CreateModel(
            name='SelfGoverningSi',
            fields=[
                ('socialdistancelevelofregion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='socialDistance.socialdistancelevelofregion')),
            ],
            bases=('socialDistance.socialdistancelevelofregion',),
        ),
        migrations.CreateModel(
            name='Si',
            fields=[
                ('socialdistancelevelofregion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='socialDistance.socialdistancelevelofregion')),
            ],
            bases=('socialDistance.socialdistancelevelofregion',),
        ),
    ]
