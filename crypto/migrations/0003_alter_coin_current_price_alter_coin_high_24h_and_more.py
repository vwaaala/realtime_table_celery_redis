# Generated by Django 4.0.3 on 2022-03-18 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0002_alter_coin_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='current_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='high_24h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='low_24h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='market_cap_change_24h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='market_cap_change_percentage_24h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='market_cap_rank',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='price_change_24h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='price_change_percentage_24h',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
