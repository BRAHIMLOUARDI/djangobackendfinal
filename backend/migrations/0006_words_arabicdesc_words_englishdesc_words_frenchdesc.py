# Generated by Django 4.0.4 on 2022-06-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_remove_words_arabicdesc_remove_words_englishdesc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='words',
            name='ArabicDesc',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='words',
            name='EnglishDesc',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='words',
            name='FrenchDesc',
            field=models.CharField(default=' ', max_length=1000),
        ),
    ]
