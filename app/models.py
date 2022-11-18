from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField()
    description = models.TextField()
    length = models.DurationField()
    path = models.CharField(max_length=500)

    def __str__(self):
        return self.title +' - '+self.date

class Sequence(models.Model):
    title = models.CharField(max_length=500)
    length = models.DurationField()
    image = models.CharField(max_length=500)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.title +' - '+self.video


class Comment(models.Model):
    content = models.TextField()
    sequence = models.ForeignKey(Sequence, on_delete=models.CASCADE)