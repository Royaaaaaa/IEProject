# Generated by Django 2.1.5 on 2019-04-07 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP01', '0006_auto_20190405_0443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='aSize',
        ),
        migrations.AddField(
            model_name='animal',
            name='aFact',
            field=models.CharField(default='', max_length=1000),
        ),
    ]