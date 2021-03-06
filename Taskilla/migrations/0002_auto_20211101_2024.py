# Generated by Django 3.2.8 on 2021-11-01 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taskilla', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='deadline',
            field=models.DateField(blank=True, verbose_name='Дата выполнения задачи'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='priority',
            field=models.CharField(blank=True, default='low', max_length=100, verbose_name='Приоритет'),
        ),
    ]
