# Generated by Django 5.0.2 on 2024-05-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0014_travel_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='url',
            field=models.CharField(blank=True, db_column='url', default=1, help_text='URL of the travel images', max_length=255, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
