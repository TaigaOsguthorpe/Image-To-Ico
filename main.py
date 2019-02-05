# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2019 Taiga Osguthorpe

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from PIL import Image
import sys
import time
import os

filename = sys.argv[1]
filename_ = filename.split("\\", -1)[-1].split(".")[0]
errors = 0
try:
    img = Image.open(filename)
except Exeption:
    print("File is not an Image file or File Is Unreadable")
    time.sleep(6)
    sys.exit()

icon_sizes = [[(256,256)], [(128,128)], [(64,64)], [(32,32)], [(16,16)]]

file_path = "{0}\\{1}_Icons".format(os.getcwd(), filename_)
if not os.path.exists(file_path):
    os.makedirs(file_path)

for size in icon_sizes:
    try:
        size_ = str(size).split(",")[0].replace("[", "").replace("(", "")
        name = "{0}\\{2}-icon-{1}x{1}.ico".format(file_path, size_, filename_)
        img.save(name, sizes=size)
    except Exeption:
        print("Unexpected Error:\nCarrying on...")
        errors = errors + 1
        pass
print("\nCompleted with {0} Errors!".format(errors))
time.sleep(2)
sys.exit()
