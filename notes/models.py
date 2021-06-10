from django.db import models
from django.utils import timezone
from django_prometheus.models import ExportModelOperationsMixin


# Create your models here.


class Note(ExportModelOperationsMixin('note'), models.Model):
    note = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return "{}; Date: {}, Likes: {}".format(self.note, self.pub_date, self.likes)
