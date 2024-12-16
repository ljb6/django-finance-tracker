# Generated by Django 5.1 on 2024-12-15 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('table_id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.TextField(max_length=80)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('table_id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.TextField(max_length=80)),
                ('date', models.DateField()),
                ('id', models.IntegerField()),
                ('category', models.TextField()),
                ('description', models.TextField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
