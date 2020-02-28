# Generated by Django 2.2.9 on 2020-02-26 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_deletedtrade'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedTrade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('deleted_trade', models.CharField(max_length=16)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateTimeField()),
                ('notional_amount', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('maturity_date', models.DateField()),
                ('underlying_price', models.FloatField()),
                ('strike_price', models.FloatField()),
                ('buying_party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deleted_buyer', to='api.Company')),
                ('notional_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deleted_notional', to='api.Currency')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deleted_product', to='api.Product')),
                ('selling_party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deleted_seller', to='api.Company')),
                ('underlying_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deleted_underlying', to='api.Currency')),
            ],
            options={
                'db_table': 'deleted_trade',
            },
        ),
    ]