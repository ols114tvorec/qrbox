from django.db import models
from . choices import STATUSES
import uuid
from . managers import QRcodeManager
class QRCode(models.Model):
    image = models.ImageField(upload_to='')
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    zone = models.ForeignKey('QRZone', on_delete=models.CASCADE, null=True)
    objects = models.Manager()
    active_objects = QRcodeManager()

class QRZone(models.Model):
    name = models.CharField(max_length=128)
    
class Feedback(models.Model):
    text = models.CharField(max_length=512)
    name = models.CharField(max_length=128)
    contact = models.CharField(max_length=48)
    status = models.IntegerField(choices=STATUSES,default=1)
