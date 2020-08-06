import qrcode

im = qrcode.make("daba.jpg")
im.save("qr3.png", "PNG")
