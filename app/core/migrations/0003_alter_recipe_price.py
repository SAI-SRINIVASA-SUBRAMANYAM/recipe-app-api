# Generated by Django 3.2.18 on 2023-02-25 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
