# Generated by Django 3.2.5 on 2021-07-26 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data',
            field=models.CharField(max_length=10),
        ),
    ]
