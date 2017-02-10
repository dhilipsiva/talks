#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: audio.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2017-02-10
"""

from pydub import AudioSegment
song = AudioSegment.from_wav("trance.wav")

# pydub does things in miliseconds
ten_seconds = 10 * 1000
first_10_seconds = song[ten_seconds:ten_seconds*2]
last_5_seconds = song[-5000:]

# boost volume by 6dB
beginning = first_10_seconds + 6
# reduce volume by 3dB
end = last_5_seconds - 3

# without_the_middle = beginning + end

# song is not modified
backwards = beginning.reverse()


with_style = beginning.append(end, crossfade=1500)
with_style = with_style.append(backwards, crossfade=1500)
do_it_over = with_style * 2

awesome = do_it_over.fade_in(2000).fade_out(3000)

awesome.export("mashup.wav", format="wav")
