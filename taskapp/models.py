from django.db import models




# Create your models here.
class place(models.Model):

    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='site_pics')
    details = models.TextField()

    def __str__(self):
        return self.name

class people(models.Model):

    name1 = models.CharField(max_length=250)
    img1 = models.ImageField(upload_to='site_pics')
    details1 = models.TextField()
    def __str__(self):
        return self.name1