#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: create_file.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-11-22
"""

import re
import os
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')


input_text = input("Enter date [%s]: " % today)
if input_text == '':
    input_text = today

file_name = input_text
assets_dir = "assets/%s" % input_text

if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)

input_texts = []
while True:
    input_text = input("Enter text / simply press enter to quit: ")
    if input_text == '':
        break
    input_text = input_text.lower()
    input_texts.append(input_text.lower())

for input_text in input_texts:
    input_text = re.sub('[^0-9a-z]+', '-', input_text)
    input_text = input_text.title()
    file_name = "%s-<%s>" % (file_name, input_text)

file_name = "%s.md" % file_name

with open("README.md") as readme:
    with open(file_name, "w") as slide:
        slide.write(readme.read() % locals())

print("Created Folder: %s" % assets_dir)
print("Created Slide: %s" % file_name)
