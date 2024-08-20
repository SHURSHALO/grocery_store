# Generated by Django 4.2.15 on 2024-08-19 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_alter_product_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image_large",
            field=models.ImageField(upload_to="post_images/large/"),
        ),
        migrations.AlterField(
            model_name="product",
            name="image_medium",
            field=models.ImageField(upload_to="post_images/medium/"),
        ),
        migrations.AlterField(
            model_name="product",
            name="image_small",
            field=models.ImageField(upload_to="post_images/small/"),
        ),
    ]
