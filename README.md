# QR-code-generation
''' 
What is QR code ? 
A Quick Response code is a two-dimensional pictographic code used for its fast readability and comparatively large storage capacity. 
The code consists of black modules arranged in a square pattern on a white background. The information encoded can be made up of any kind
of data (e.g., binary, alphanumeric, or Kanji symbols).

-------------------------
Now let's see how to generate QR code  using python .
It's very simple to generate the QR code by importing qrcode module. 

First to generate a QR code you should have qrcode module installed in the system. 

If qrcode module is not installed, install it using pip command. Use the followwing command in the command prompt
 
    pip install qrcode

In the following code, make() generates the qrcode and stores in im variable
the image generated we save in the system in the name 'qr.png' in png formate
You can find the your QR code image in the directory you saved your code. 
Data can be any video or text or any file. For any data QR will be generated.
'''

import qrcode

im = qrcode.make("any data here !")  # can keep any data

im.save("qr.png", "PNG")
