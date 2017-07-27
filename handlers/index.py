#!/usr/bin/env python
# coding=utf-8

import tornado.web
import json
import os

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        text = self.get_argument("text")
        text_file =file('text.txt','w')
        print text
        text_file.write(text)
        text_file.close()
      
       # text_file=file('text.txt')
       # while True:
       #     line = text_file.readline()
       #     if len(line) == 0:
       #         break
       #     print line,
       # text_file.close()
	#json_string = {}
	#json_string['text'] = text
	#if json_string:
         #filepath = './jsonfile.conf'
         #if os.path.exists(filepath):
           #os.remove(filepath)
         #ff = open(filepath, 'w')
         #json.dump(json_string, ff)  
         #ff.close()


        #文件下载
	#filename = "jsonfile.conf"
        

