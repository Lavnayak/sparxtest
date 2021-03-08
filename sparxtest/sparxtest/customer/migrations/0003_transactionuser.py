# Generated by Django 3.1.7 on 2021-03-07 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_myuser_account_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('account_no', models.CharField(max_length=100)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('1', 'Deposit'), ('2', 'Withdraw')], max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created On')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
