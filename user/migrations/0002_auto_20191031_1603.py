# Generated by Django 2.2.3 on 2019-10-31 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='postalcode',
            field=models.IntegerField(default=0, max_length=11),
        ),
    ]