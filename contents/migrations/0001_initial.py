# Generated by Django 4.1.7 on 2023-03-28 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('images', models.ImageField(upload_to='brand_image/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('images', models.ImageField(upload_to='category_image/')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('color_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Smartphone_RAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Smartphone_Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('images', models.ImageField(upload_to='smartphone_image/')),
                ('specification', models.TextField()),
                ('model_name', models.CharField(max_length=255)),
                ('screen_size', models.CharField(max_length=255)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.brand')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.color')),
                ('ram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.smartphone_ram')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.smartphone_storage')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('images', models.ImageField(upload_to='products_image/')),
                ('status', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.category')),
                ('smartphone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.smartphone')),
            ],
        ),
    ]
