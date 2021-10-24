# Generated by Django 3.2.8 on 2021-10-20 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SellOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]