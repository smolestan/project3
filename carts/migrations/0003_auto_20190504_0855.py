# Generated by Django 2.0.3 on 2019-05-04 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_auto_20190504_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='topping2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='topping3',
            field=models.TextField(blank=True, null=True),
        ),
    ]