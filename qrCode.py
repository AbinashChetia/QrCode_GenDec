# Author: Abinash Chetia
# Dated: 12/02/2021

import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
from tkinter.filedialog import * # pylint: disable=unused-import

opt = 0
print("\tQR CODE GENERATOR & DECODER:")
while opt != 3:
    print("\nOptions:\n\t1. Generate QR code for input text.\n\t2. Decode QR code.\n\t3. Exit.")
    opt = int(input("\nYour choice (1/2/3): "))

    if opt == 1:
        text = input("\nEnter message: ")
        qr = pyqrcode.create(text)
        savePath = asksaveasfilename()
        qr.png(savePath+".png", scale=8)

    elif opt == 2:
        filePath = askopenfilename()
        d = decode(Image.open(filePath))
        print("\nDecoded message: "+d[0].data.decode("ascii"))

    elif opt == 3:
        print("\nExiting the program.\n")

    else:
        print("\nInvalid input.")