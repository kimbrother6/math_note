from django.db import models


class Post(models.Model):
    book = models.CharField(max_length=50, null = True, blank = True)
    page = models.IntegerField(null=True)
    number = models.IntegerField(null=True)
    WR = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.WR
