# from qrtools import qrtools,QR
# qr = qrtools.QR()
# qr.decode("horn.png")
# print(qr.data)



from pyzbar.pyzbar import decode
from PIL import Image
print(decode(Image.open('horn1.png')))