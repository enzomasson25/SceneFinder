from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField(auto_now=True)
    description = models.TextField()
    length = models.DurationField(null=True,blank=True)
    path = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title +' - '+str(self.date)

class Sequence(models.Model):
    title = models.CharField(max_length=500)
    length = models.DurationField()
    image = models.ImageField(upload_to='images/')
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.title +' - '+ str(self.video)


class Comment(models.Model):
    content = models.TextField()
    sequence = models.ForeignKey(Sequence, on_delete=models.CASCADE)