# Generated by Django 4.0.5 on 2022-06-09 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
