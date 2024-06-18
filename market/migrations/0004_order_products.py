# Generated by Django 5.0.6 on 2024-06-18 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_client_password_delivery_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='market.product'),
        ),
    ]
