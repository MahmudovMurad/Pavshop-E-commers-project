# Generated by Django 3.2.6 on 2021-11-19 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20211118_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, db_index=True, null=True, related_name='product_category', to='store.Category'),
        ),
    ]
