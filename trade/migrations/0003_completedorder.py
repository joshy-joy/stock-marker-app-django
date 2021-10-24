# Generated by Django 3.2.8 on 2021-10-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20211020_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
            ],
        ),
    ]
