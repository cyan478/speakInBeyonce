import csv 
import re
import urllib2
import json
import csv
import codecs
import os
import socket
from socket import AF_INET, SOCK_DGRAM
import sys
# sys.path.insert(0, 'lyrics-search')
from search import *

def prep(csvFileName): # preps csv file
    inStream = open(csvFileName,"r")
    demo = inStream.readlines()
    inStream.close()


    x=1
    ret=[]
    while x<len(demo):
        demo[x]=demo[x].split(',')
        ret.append(demo[x][1])
        x+=1
    return ret


def load_credentials():
    lines = [line.rstrip('\n') for line in open('credentials.ini')]
    chars_to_strip = " \'\""
    for line in lines:
        if "client_id" in line:
            client_id = re.findall(r'[\"\']([^\"\']*)[\"\']', line)[0]
        if "client_secret" in line:
            client_secret = re.findall(r'[\"\']([^\"\']*)[\"\']', line)[0]
        #Currently only need access token to run, the other two perhaps for future implementation
        if "client_access_token" in line:
            client_access_token = re.findall(r'[\"\']([^\"\']*)[\"\']', line)[0]
    return client_id, client_secret, client_access_token


def findRef(id, client_access_token):
    querystring = "http://api.genius.com/referents?song_id=" + id + "&text_format=html&per_page=1"
    request = urllib2.Request(querystring)
    request.add_header("Authorization", "Bearer " + client_access_token)   
    request.add_header("User-Agent", "curl/7.9.8 (i686-pc-linux-gnu) libcurl 7.9.8 (OpenSSL 0.9.6b) (ipv6 enabled)") #Must include user agent of some sort, otherwise 403 returned
    return request

#print prep("lyrics-search\output\output-yahMainbitchoutyourleaguetooahSidebitchoutofyourleaguetooah.csv")
client_id, client_secret, client_access_token = load_credentials()
#print findRef(prep("lyrics-search\output\output-yahMainbitchoutyourleaguetooahSidebitchoutofyourleaguetooah.csv")[0],client_access_token)