# Generated by Django 4.0.4 on 2022-08-06 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0003_ingredient_plat'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='Photo',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]