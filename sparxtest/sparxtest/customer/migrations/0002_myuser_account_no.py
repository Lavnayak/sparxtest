# Generated by Django 3.1.7 on 2021-03-07 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='account_no',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]