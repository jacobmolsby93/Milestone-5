# Generated by Django 3.2.9 on 2021-11-25 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20211122_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='sku',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
