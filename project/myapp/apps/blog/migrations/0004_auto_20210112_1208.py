# Generated by Django 3.1.5 on 2021-01-12 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210111_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='outstandingType1',
            field=models.BooleanField(default=False, verbose_name='Destacado tipo 1  SI/ NO'),
        ),
        migrations.AddField(
            model_name='post',
            name='outstandingType2',
            field=models.BooleanField(default=False, verbose_name='Destacado tipo 2  SI/ NO'),
        ),
    ]
