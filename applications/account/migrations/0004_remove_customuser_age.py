# Generated by Django 4.2.5 on 2023-09-05 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_customuser_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
    ]
