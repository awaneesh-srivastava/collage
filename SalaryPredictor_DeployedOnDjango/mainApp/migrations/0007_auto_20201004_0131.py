# Generated by Django 3.1.1 on 2020-10-03 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_remove_userhistory_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhistory',
            name='date',
            field=models.DateField(),
        ),
    ]