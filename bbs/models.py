from django.db import models
from django.utils import timezone

class Topic(models.Model):

    class Meta:
        db_table = "topic"

    name        = models.CharField(verbose_name="投稿者の名前",max_length=100)
    comment     = models.CharField(verbose_name="コメント",max_length=2000)
    dt          = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)

    def __str__(self):
        return self.comment
