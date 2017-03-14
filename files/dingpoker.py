"""
dingpoker.py
pokes the irods set up and parses the info into a json reply.
"""
import json
import time
import socket
from irods.miscsvrinfo import iMiscSvrInfo
def parse(info):
    '''
    The results of the imiscsvrinfo query are encoded
    as attributes of an object.
    Here we parse those attributes into a dict
    which is then parsed into a json object to for dingrod to send back.
    '''
    mdict = {
        'serverType' : info.serverType,
        'relVersion' : info.relVersion,
        'apiVersion' : info.apiVersion,
        'rodsZone'   : info.rodsZone,
        'uptime'     : int(info.serverBootTime - int(time.time()))
        }
    return  json.JSONEncoder().encode(mdict)

def poke(host, port):
    '''
    this function executes the actual poke,
    obtaining an iMiscSvrInfo object from the python irods client.
    We parse the object into a json message for dingrod to return
    '''
    try:
        info = iMiscSvrInfo(host, port)
        return parse(info)
    except socket.error:
        return None
