# Generated by Django 2.2.7 on 2019-12-04 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=9)),
                ('stock', models.IntegerField()),
                ('selling_price', models.IntegerField()),
            ],
        ),
    ]
