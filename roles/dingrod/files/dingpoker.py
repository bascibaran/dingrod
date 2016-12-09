import json
import os
import subprocess as sp

def parse(resp):
  slist = resp.split('\n')
  sdict = slistToDict(slist)
  return  json.JSONEncoder().encode(sdict)
  

def slistToDict(slist):
  rdict = {}
  for i in range(1,4):
    kvpair = slist[i].split('=')
    rdict[kvpair[0]] = kvpair[1]  
  upsplit = slist[4].split()
  upstr   = upsplit[1] + ":" + upsplit[3]
  rdict['uptime'] =  upstr
  return rdict
 
  

def poke():
  try:
    sp.check_call(["/var/lib/dingrod/icommands/imiscsvrinfo"])
    return parse(os.popen("/var/lib/dingrod/icommands/imiscsvrinfo").read())
  except sp.CalledProcessError:
    return None


  
