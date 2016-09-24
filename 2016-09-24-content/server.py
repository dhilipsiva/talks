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
Date created: 2016-09-10
"""

import subprocess
import http.server

VERSION = 1


class SimpleHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        hostname = subprocess.check_output('hostname')
        body = b"version(%d): %b" % (VERSION, hostname)
        self.wfile.write(body)

address = ('0.0.0.0', 8000)
server = http.server.HTTPServer(address, SimpleHandler)
print('Started http server')
server.serve_forever()
