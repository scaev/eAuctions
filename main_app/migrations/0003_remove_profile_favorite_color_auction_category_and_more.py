# Generated by Django 4.1.6 on 2023-02-16 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_auction_options_alter_bid_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='favorite_color',
        ),
        migrations.AddField(
            model_name='auction',
            name='category',
            field=models.CharField(choices=[('antiques', 'ANTIQUES'), ('art', 'ART'), ('electronics', 'ELECTRONICS'), ('furniture', 'FURNITURE'), ('jewelry', 'Jewelry'), ('tools', 'TOOLS'), ('others', 'OTHERS')], default='others', max_length=11),
        ),
        migrations.AddField(
            model_name='auction',
            name='condition',
            field=models.CharField(choices=[('new', 'NEW'), ('used', 'USED'), ('refurbished', 'REFURBISHED')], default='used', max_length=11),
        ),
    ]
