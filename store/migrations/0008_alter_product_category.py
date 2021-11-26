# Generated by Django 3.2.6 on 2021-11-19 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('store', '0007_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, db_index=True, null=True, related_name='product_category', to='core.Category'),
        ),
    ]
