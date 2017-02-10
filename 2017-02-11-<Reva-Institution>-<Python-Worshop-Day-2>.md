<!--
$theme: gaia
template: invert
-->

# Python Workshop Day 2

## REVA Institutions

## [@dhilipsiva](https://github.com/dhilipsiva)

--- 

# Requirements

```
pip install xlsxwriter pydub pillow moviepy 
```

---

- Tech Lead, Full-Stack & DevOps - [@Appknox](https://twitter.com/appknox)
- I code for Web, Mobile, Embedded & IoT. Open-Source Fanatic. Big Data & Machine Learning Enthusiast. Dad. Atheist
- So primarily a Developer + little bit of this & that
- Jack of all trades & Master of none
- No, I do not keep Bindi for religious reasons. Its for a scientific reason & a fashion statement.
- [http://dhilipsiva.com](http://dhilipsiva.com)
- [dhilipsiva@gmail.com](mailto:dhilipsiva@gmail.com)

---

# I have no idea what I am talking about :stuck_out_tongue_winking_eye:

---

# How else can I help you?

- Dropout (Yes, I am not a graduate)
- Startup Fanatic (& hate corporate)
- Full Stack & DevOps landscape
- Getting Started on ML
- I love Python. A lot.
- Take my words with a pinch of salt

---

# Recap: Workshop Day 1

None, Boolean, Numbers, Strings, List, Tuple, Set, Dict, Variables, List & String Manipulation, Conditionals, Loops, Function

More: https://github.com/ChillarAnand/python-101/blob/master/manuscript.md

---

# Overview: Workshop Day 2

* Files (Text, [Excel](https://github.com/jmcnamara/XlsxWriter), [Audio](http://pydub.com/), [Image](https://python-pillow.org/), [Video](https://github.com/Zulko/moviepy))
* Classes & Objects
* CLI Application (Let's build a simple game)

---

# Files

```py
fr = open("file.txt")  # Open a file to read
fr.read()  # Will read entire content
fr.readline()  # Reads line by line
fr.readlines()  # Reads the entire files and return a list
fr.close()  # Close the file

fw = open("file.txt", "w")  # Open a file to write
fw.write("Foo Bar")  # Write a single line
fw.writelines(["One", "Two"])  # Write a list of lines
fw.close()  # Close the file 

# Also explain append mode
```
---

## Excercises

1. Copy content of one file into another file
2. Remove the lines in a file which has the text `foo`

---

## Excel Sheet

```py
import xlsxwriter

workbook = xlsxwriter.Workbook('demo.xlsx') 
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 20) 
bold = workbook.add_format({'bold': True}) 
worksheet.write('A1', 'Hello')  
worksheet.write('A2', 'World', bold) 
worksheet.write(2, 0, 123) 
worksheet.write(3, 0, 123.456)
worksheet.insert_image('B5', 'logo.png')
workbook.close()
```

---

## Image

```py
from PIL import ImageFilter
size = (128, 128)
from PIL import Image
im = Image.open("lena.ppm")
print(im.format, im.size, im.mode)
im.show()
im.thumbnail(size)
box = (100, 100, 400, 400)
region = im.crop(box)
region = region.transpose(Image.ROTATE_180)
out = im.resize((128, 128))
out = im.rotate(45)
out = im.transpose(Image.FLIP_LEFT_RIGHT)
out = im.filter(ImageFilter.DETAIL)
```
---

## Audio

```py
from pydub import AudioSegment
song = AudioSegment.from_wav("trance.wav")
ten_seconds = 10 * 1000
first_10_seconds = song[ten_seconds:ten_seconds*2]
last_5_seconds = song[-5000:]
beginning = first_10_seconds + 6
end = last_5_seconds - 3
backwards = beginning.reverse()
with_style = beginning.append(end, crossfade=1500)
with_style = with_style.append(backwards, crossfade=1500)
do_it_over = with_style * 2
awesome = do_it_over.fade_in(2000).fade_out(3000)
awesome.export("mashup.wav", format="wav")
```

---

## Video
```
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
clip = VideoFileClip("baby-cry.webm")
clip = clip.volumex(0.8)
txt_clip = TextClip("Baby Cry", fontsize=70, color='white')
txt_clip = txt_clip.set_pos('center').set_duration(3)
video = CompositeVideoClip([clip, txt_clip])
video.write_videofile("baby-cry-text.webm")
```

---

# Classes and Objects

* Abstraction
* Polymorphism
* Encapsulation
* Inheritance

\_\_init__, super, \_\_str__, \_\_len__

---

# CLI Applications

Lets build a simple game, shall we?

---

# Thanks! :pray:

### https://github.com/dhilipsiva/talks

This copy is released under the [MIT License](https://github.com/dhilipsiva/talks/blob/master/LICENSE)

[Source Code](https://github.com/dhilipsiva/talks/blob/master/2017-02-11-<Reva-Institution>-<Python-Worshop-Day-2>.md)
[SlideShare Link](http://www.slideshare.net/dhilipsiva/slide)

# Questions:question:
[http://dhilipsiva.com](http://dhilipsiva.com)
