# Generated by Django 4.2 on 2024-07-11 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0004_author_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
