# Generated by Django 2.2.3 on 2020-03-07 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=100)),
                ('ingredients', models.CharField(max_length=1000)),
            ],
        ),
    ]
