# Generated by Django 2.1.5 on 2019-05-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
            ],
        ),
    ]