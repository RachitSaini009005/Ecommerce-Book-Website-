# Generated by Django 4.1.3 on 2024-05-11 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Books_author_book_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('authors', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=13)),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cover_image', models.ImageField(upload_to='book_covers/')),
                ('publisher', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=50)),
                ('number_of_pages', models.PositiveIntegerField()),
                ('format', models.CharField(max_length=50)),
                ('edition', models.CharField(blank=True, max_length=50, null=True)),
                ('keywords', models.CharField(max_length=255)),
                ('availability', models.CharField(max_length=50)),
            ],
        ),
    ]
