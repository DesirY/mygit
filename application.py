#!/usr/bin/env python
# coding=utf-8

import tornado.web
import os
from handlers.index import IndexHandler
from handlers.down import DownHandler

settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__),"statics")
    )

application = tornado.web.Application(
    handlers = [(r'/',IndexHandler),
               (r'/down',DownHandler)],
    **settings
    )
