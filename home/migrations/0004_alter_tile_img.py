# Generated by Django 4.1 on 2023-02-26 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_customer_delete_booker_tile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tile',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
