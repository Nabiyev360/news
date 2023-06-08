# Generated by Django 4.2.2 on 2023-06-06 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'verbose_name_plural': 'Yangiliklar'},
        ),
        migrations.AlterField(
            model_name='new',
            name='photo',
            field=models.IntegerField(blank=True, null=True, verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='new',
            name='text',
            field=models.TextField(verbose_name='Yangilik matni'),
        ),
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(max_length=1000, verbose_name='Sarlavha'),
        ),
        migrations.AlterField(
            model_name='new',
            name='video',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Video link'),
        ),
    ]
