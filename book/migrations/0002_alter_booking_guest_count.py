# Generated by Django 4.2.7 on 2024-07-16 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='guest_count',
            field=models.PositiveBigIntegerField(choices=[(1, '1 Guest'), (2, '2 Guests'), (3, '3 Guests'), (4, '4 Guests'), (5, '5 Guests'), (6, '6 Guests')], default=4),
        ),
    ]
