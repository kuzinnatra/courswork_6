from django.db import models

NULLABLE = {"blank": True, "null": True}

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя", help_text="(при наличии)", **NULLABLE,)
    email_client = models.EmailField(verbose_name="электронная почта",help_text="(обязятельно)", unique=True,)
    def __str__(self):
        return f'{self.email_client} ({self.name})'
    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"
        ordering = ('email_client',)


class Letter(models.Model):
    title = models.CharField(max_length=150, verbose_name="Тема письма",)
    body = models.TextField(verbose_name='содержимое')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'