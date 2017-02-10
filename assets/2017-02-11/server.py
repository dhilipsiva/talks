#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: server.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2017-02-11
"""

from os import curdir
from os.path import join as pjoin

from http.server import BaseHTTPRequestHandler, HTTPServer


class GameHandler(BaseHTTPRequestHandler):
    store_path = pjoin(curdir, 'game.txt')

    def do_POST(self):
        length = self.headers['content-length']
        data = self.rfile.read(int(length))

        with open(self.store_path, 'w') as fh:
            fh.write(data.decode())

        self.send_response(200)


server = HTTPServer(('', 8080), GameHandler)
server.serve_forever()
