from django.db import models
# Create your models here.

def func():
    return 'new'

class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Заголовок")
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name="Заголовок")
    detailed_description = models.TextField(max_length=3000, null=True, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=50, default=func(), null=False, blank=False, verbose_name="Автор")
    ended_at = models.DateTimeField(verbose_name="Срок выполнения")

    def __str__(self):
        return f'{self.title} - {self.description}'