# Generated by Django 3.2.7 on 2021-09-16 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0006_auto_20181115_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
