# Generated by Django 3.2 on 2021-04-17 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Controller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id_group', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
