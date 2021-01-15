# Generated by Django 3.1.5 on 2021-01-15 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210112_1208'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-creationDate'], 'verbose_name': 'Artículo', 'verbose_name_plural': 'Artículos'},
        ),
        migrations.AlterField(
            model_name='category',
            name='creationDate',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
    ]