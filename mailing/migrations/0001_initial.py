# Generated by Django 5.1.1 on 2024-09-24 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='введите имя клиента', max_length=100, null=True, verbose_name='Имя клиента')),
                ('email_client', models.EmailField(max_length=254, unique=True, verbose_name='электронная почта')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
                'ordering': ('email_client',),
            },
        ),
    ]
