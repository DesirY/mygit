#!/usr/bin/env python
# coding=utf-8

import tornado.web 
import os

class DownHandler(tornado.web.RequestHandler):
    def get(self):
	self.set_header ('Content-Type', 'application/octet-stream')
        self.set_header ('Content-Disposition', 'attachment; filename=text.txt')
        buf_size = 1024
        with open(os.path.join('','text.txt'), 'rb') as f:
            while True:
                data = f.read(buf_size)
                if not data:
                    break
                self.write(data)
        self.finish()

