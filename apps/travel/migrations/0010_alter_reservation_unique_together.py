# Generated by Django 5.0.2 on 2024-04-03 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0009_alter_reservation_rating'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together={('travel', 'passenger')},
        ),
    ]
