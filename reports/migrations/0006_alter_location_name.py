# Generated by Django 4.2.1 on 2024-12-10 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_location_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
