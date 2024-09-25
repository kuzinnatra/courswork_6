# Generated by Django 5.1.1 on 2024-09-25 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email_client',
            field=models.EmailField(max_length=254, unique=True, verbose_name='электронная почта *'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(blank=True, help_text='введите имя получателя рассылки', max_length=100, null=True, verbose_name='Имя'),
        ),
    ]
