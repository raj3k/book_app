# Generated by Django 4.0.3 on 2022-04-02 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_isbn_alter_book_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of pages in the book'),
        ),
    ]