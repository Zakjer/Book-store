# Generated by Django 4.2 on 2023-06-19 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product_image_delete_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(default=1004, on_delete=django.db.models.deletion.CASCADE, to='shop.customer'),
        ),
    ]