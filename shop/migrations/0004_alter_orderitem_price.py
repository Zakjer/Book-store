# Generated by Django 4.2 on 2023-06-03 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_customer_options_remove_customer_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
