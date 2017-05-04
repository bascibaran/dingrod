#!/usr/bin/python
import sys
import datetime   as dt
import dingpoker  as dp
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import json

PORT_NUMBER = 20500

HOST = 'localhost'
PORT = '1247'

class pingHandler(BaseHTTPRequestHandler):
  lastping  = None
  ding      = None

  def do_GET(self):
    if self.lastping is None:
      self.lastping = dt.datetime.now()
      self.ding = dp.poke(HOST,PORT)
    else:
      tnow = dt.datetime.now()
      tdelt = tnow - lastping
      if tdelt.total_seconds > 1:
        self.lastping = tnow
        self.ding = dp.poke(HOST,PORT)
    if self.ding is not None:
    #return 200 and json object stored as string in ding
      self.send_response(200)
      self.send_header('Content-Type','application/json')
      self.end_headers()
      self.wfile.write(self.ding)
    else:
    #return 503
      self.send_response(503)
    return

def serve():
  server = HTTPServer(('',PORT_NUMBER), pingHandler)
  while True:
    server.handle_request()

if __name__ == "__main__":
  if (len(sys.argv) > 2):
    PORT_NUMBER = int(sys.argv[1]);
    IRODS_ENV   = sys.argv[2];
  with open(IRODS_ENV) as json_data:
    d = json.load(json_data)
    HOST = d['irods_host']
    PORT = d['irods_port']
  serve()
