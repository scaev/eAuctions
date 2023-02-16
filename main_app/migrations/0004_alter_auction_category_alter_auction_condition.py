# Generated by Django 4.1.6 on 2023-02-16 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_profile_favorite_color_auction_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='category',
            field=models.CharField(choices=[('Antiques', 'ANTIQUES'), ('Art', 'ART'), ('Electronics', 'ELECTRONICS'), ('Furniture', 'FURNITURE'), ('Jewelry', 'JEWELRY'), ('Tools', 'TOOLS'), ('Others', 'OTHERS')], default='others', max_length=11),
        ),
        migrations.AlterField(
            model_name='auction',
            name='condition',
            field=models.CharField(choices=[('New', 'NEW'), ('Used', 'USED'), ('Refurbished', 'REFURBISHED')], default='used', max_length=11),
        ),
    ]