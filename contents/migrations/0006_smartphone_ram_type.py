# Generated by Django 4.1.7 on 2023-04-04 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0005_alter_smartphone_specification'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphone_ram',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]