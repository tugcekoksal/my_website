# Generated by Django 3.0.7 on 2020-07-07 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20200705_0133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
    ]
