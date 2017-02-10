#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: make_request.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2017-02-11
"""

import requests


data = """
xxx
xxx
xxx
"""

requests.post("http://localhost:8080",  data=data)
