from django.db import models


# Create your models here.
class ZufangInfo(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    money = models.CharField(max_length=100)
    method = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    community = models.CharField(max_length=100)
    targeturl = models.CharField(max_length=100)
    pub_time = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    img1 = models.CharField(max_length=100)
    img2 = models.CharField(max_length=100)
