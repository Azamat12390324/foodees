# Generated by Django 4.2.4 on 2023-10-18 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left_image', models.ImageField(upload_to='media/about/left_image/%Y%m/%d')),
                ('about_title', models.CharField(max_length=255)),
                ('article', models.CharField(max_length=255)),
                ('article_author', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icons', models.ImageField(upload_to='media/Feature/icons/%Y%m/%d')),
                ('title', models.CharField(max_length=25)),
                ('sub_title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(upload_to='media/banner/%Y%m/%d')),
                ('title', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Menu_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icons', models.ImageField(upload_to='media/Menu_Category/icons/%Y%m/%d')),
                ('title', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icons', models.ImageField(upload_to='media/Menu/icons/%Y%m/%d')),
                ('title', models.CharField(max_length=25)),
                ('sub_title', models.CharField(max_length=255)),
                ('food_name', models.CharField(max_length=255)),
                ('food_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('food_image', models.ImageField(upload_to='media/Menu/food_image/%Y%m/%d')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.menu_category')),
            ],
        ),
    ]