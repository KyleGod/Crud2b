# Generated by Django 4.2.11 on 2024-07-05 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_item_birthday_item_blood_type_item_citizenship_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='occupation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
