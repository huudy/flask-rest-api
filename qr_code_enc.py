import pyqrcode
# url = pyqrcode.create('http://uca.edu')
# url.svg('uca-url.svg', scale=8)
# url.eps('uca-url.eps', scale=2)
# print(url.terminal(quiet_zone=1))


qr = pyqrcode.create('http://uca.edu', error='H')
qr.png("horn1.png", scale=6)