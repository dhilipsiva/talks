#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: image.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2017-02-10
"""

from PIL import ImageFilter
# size = (128, 128)
from PIL import Image
im = Image.open("corgi.jpg")
print(im.format, im.size, im.mode)
# im.show()
# im.thumbnail(size)
box = (1400, 500, 2000, 1000)
region = im.crop(box)
# region = region.transpose(Image.ROTATE_180)
region = region.transpose(Image.FLIP_LEFT_RIGHT)
region.resize((128, 128))
# region = region.filter(ImageFilter.DETAIL)
region = region.filter(ImageFilter.BLUR)
region.show()
# out = im.rotate(45)  # degrees counter-clockwise
