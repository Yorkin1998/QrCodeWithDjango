from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
import qrcode
# Create your models here.
class Students(models.Model):
    name_and_surname = models.CharField(max_length=255, db_index=True)
    passport_number = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.passport_number


class QrCodes(models.Model):
    which = models.ForeignKey(Students, on_delete=models.CASCADE)
    qrcodes = models.ImageField(upload_to='static/QrCodes/')

    def __str__(self):
        return str(self.which)


# Create your views here.

@receiver(post_save, sender=Students)
def update_post(sender, instance, created, **kwargs):
    if created:
        data = str(instance)
        img = qrcode.make(data)
        img.save(f"static/QrCodes/{data}.png")
        QrCodes.objects.create(which=Students.objects.get(passport_number=instance),qrcodes=f"static/QrCodes/{data}.png")


