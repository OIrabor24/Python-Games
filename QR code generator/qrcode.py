import pyqrcode 

data = input("Enter the text or link to generate qr code: ") 
# Using pyqrcode.create() to create a qr code of the input data
qr = pyqrcode.create(data) 
# Using .svg mehtod to save the qr code as SVG file of provided name & scale
generator = qr.svg('qr_code.svg', scale=8) 