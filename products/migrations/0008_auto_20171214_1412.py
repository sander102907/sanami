# Generated by Django 2.0 on 2017-12-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20171214_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('men', 'Men'), ('women', 'Women')], default='MEN', max_length=5),
        ),
    ]
