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

workbook = xlsxwriter.Workbook('demo.xlsx')  # Create an new Excel file and add a worksheet.
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 20)  # Widen the first column to make the text clearer.
bold = workbook.add_format({'bold': True})  # Add a bold format to use to highlight cells.
worksheet.write('A1', 'Hello')  # Write some simple text.
worksheet.write('A2', 'World', bold)  # Text with formatting.
worksheet.write(2, 0, 123)  # Write some numbers, with row/column notation.
worksheet.write(3, 0, 123.456)
worksheet.insert_image('B5', 'logo.png')  # Insert an image.
workbook.close()
```

---

## Audio

---

# Classes and Objects

---

# CLI Applications

---

# Thanks! :pray:

### https://github.com/dhilipsiva/talks

This copy is released under the [MIT License](https://github.com/dhilipsiva/talks/blob/master/LICENSE)

[Source Code](https://github.com/dhilipsiva/talks/blob/master/2017-02-11-<Reva-Institution>-<Python-Worshop-Day-2>.md)
[SlideShare Link](http://www.slideshare.net/dhilipsiva/slide)

# Questions:question:
[http://dhilipsiva.com](http://dhilipsiva.com)
