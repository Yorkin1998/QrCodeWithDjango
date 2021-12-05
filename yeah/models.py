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
    student_token=models.CharField(max_length=300,unique=True,blank=True,null=True)
    def __str__(self):
        return str(self.which)


# Create your views here.
import hashlib
@receiver(post_save, sender=Students)
def update_post(sender, instance, created, **kwargs):
    if created:
        mystring=f'{Students.objects.get(passport_number=instance).id}'
        hash_object = hashlib.md5(mystring.encode())
        #print(hash_object.hexdigest())
        data = f"https://b0a0-84-54-120-237.ngrok.io/{Students.objects.get(passport_number=instance).id}/{hash_object.hexdigest()}"
        x=f"{Students.objects.get(passport_number=instance).id}"
        img = qrcode.make(data)
        img.save(f"static/QrCodes/{x}.png")
        QrCodes.objects.create(which=Students.objects.get(passport_number=instance),qrcodes=f"static/QrCodes/{data}.png",student_token=hash_object.hexdigest())


