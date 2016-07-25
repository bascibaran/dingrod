#!/usr/bin/python
import logging
import subprocess as sp
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
PORT_NUMBER = 20500
class pingHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    logging.debug('received GET request')
    try:
      sp.check_call(["./monitor.sh"])
      self.send_response(200)
      logging.debug('iRODS is up')
    except sp.CalledProcessError:
      logging.debug('iRODS is down')
      self.send_response(503)
    return
def serve():
  logging.info('creating pingrod server')
  server = HTTPServer(('',PORT_NUMBER), pingHandler)
  while True:
    server.handle_request()

if __name__ == "__main__":
  serve()
