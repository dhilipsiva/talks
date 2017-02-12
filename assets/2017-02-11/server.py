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

from http.server import BaseHTTPRequestHandler, HTTPServer


class GameHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        length = self.headers['content-length']
        data = self.rfile.read(int(length))

        with open('game.txt', 'w') as fh:
            fh.write(data.decode())

        self.send_response(200)


server = HTTPServer(('', 8080), GameHandler)
print("Server is running...")
server.serve_forever()
