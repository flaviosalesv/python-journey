import qrcode

img = qrcode.make('http://youtube.com')
img.save('qrcode.png')
