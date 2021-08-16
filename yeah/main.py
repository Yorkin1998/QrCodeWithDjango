import os
import django



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject3.settings")

django.setup()
from yeah.models import Students,QrCodes
import cv2
all_list = []
finished=[]
for i in Students.objects.all():
    all_list.append(i.passport_number)
print(all_list)

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
i=0
while i<len(all_list):
    _, img = cap.read()
    data, bbox, _ = detector.detectAndDecode(img)
    if (data in all_list) and (data not in finished):
        print(Students.objects.get(passport_number=data).name_and_surname + " Here")
        finished.append(data)
        i+=1
    else:
        pass
    cv2.imshow("QRCODEscanner", img)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
# Importing library
# import qrcode
#
# # Data to be encoded
# data = 'Abdumalik'
#
# # Encoding data using make() function
# img = qrcode.make(data)
#
# # Saving as an image file
# img.save('MyQRCode1.png')
