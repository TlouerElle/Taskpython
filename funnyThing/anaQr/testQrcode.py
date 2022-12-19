# -*- coding: UTF-8 -*-
# IDE    ：PyCharm
# File   ：testQrcode.py
# Date   ：2022/3/1 9:41
# Author ：Touououououer
# E-mail  ：wes0018@aliyun.com
# Introduction ：识别二维码
import sys

import pyzbar.pyzbar as pyzbar
from PIL import Image, ImageEnhance
from pyqt5_plugins.examplebutton import QtWidgets

from ui import Ui_Form

'''
二维码识别
'''
image = "qr.png"
img = Image.open(image)
barcodes = pyzbar.decode(img)
for barcode in barcodes:
    barcodeData = barcode.data.decode("utf-8")
    print(barcodeData)
