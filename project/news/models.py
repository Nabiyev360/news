from django.db import models


class New(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Sarlavha')
    text = models.TextField(verbose_name='Yangilik matni')
    photo = models.ImageField(null=True, blank=True, verbose_name='Rasm')
    video = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Video link')

    class Meta:
        verbose_name_plural = 'Yangiliklar'

    def __str__(self):
        return self.title