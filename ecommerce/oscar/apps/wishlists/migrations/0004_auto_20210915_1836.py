# Generated by Django 3.2.7 on 2021-09-16 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlists', '0003_auto_20181115_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]