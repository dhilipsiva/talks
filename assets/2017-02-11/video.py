#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: video.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2017-02-11
"""

# Import everything needed to edit video clips
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Load baby-cry.webm
clip = VideoFileClip("baby-cry.webm")

# Reduce the audio volume (volume x 0.8)
clip = clip.volumex(0.8)

# Generate a text clip. You can customize the font, color, etc.
txt_clip = TextClip("Baby Cry", fontsize=70, color='white')

# Say that you want it to appear 10s at the center of the screen
txt_clip = txt_clip.set_pos('center').set_duration(3)

# Overlay the text clip on the first video clip
video = CompositeVideoClip([clip, txt_clip])

# Write the result to a file (many options available !)
video.write_videofile("baby-cry-text.webm")
