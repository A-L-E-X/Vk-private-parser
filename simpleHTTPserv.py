#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer, os
# -*- coding: utf-8 -*-

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        if self.path == '/plot':
        	os.system(/vkchase/server_debug/plot_metric.py)
        	self.path = '/plot.html'

        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler
server = SocketServer.TCPServer(('127.0.0.1', 8080), Handler)

server.serve_forever()