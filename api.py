#!/usr/bin/python
import requests
import json
import sys


class openstack_api:
    def __init__(self, name):
        self.__name__ = name
        print 'Created trax_api successfully'
    #GET
    def get(self, url):
        print '==========Sending Request=========='
        print '[GET]'
        print '(' + url + ')'
        r = requests.get(url)
        #check response 
        if (r.ok):
            print 'code:', r.status_code
            #convert json to python form
            data = json.loads(r.text or r.content)
            #print type(data) #dic
            #JSON form
            json_out = json.dumps(data, sort_keys=True, indent=4)
            print '-----'*10, 'JSON OUT', '-----'*10
            print json_out
            print '-----'*10, 'JSON END', '-----'*10
        else:
            print "Error: Unreachable to the host", 'url'
            print 'code:', r.status_code

    #POST
    def send(self, url, payload, headers):
        print '==========Sending Request=========='
        print '[POST]'
        print '(' + url + ')'
        data=json.dumps(payload)
         #print '-----'*10, 'INPUT DATA', '-----'*10
        print 'Header:', headers
        print 'Data:', data
        #print '-----'*10, 'INPUT END', '-----'*10
        
        r = requests.post(url, data, headers=headers)
        #check response 
        if (r.ok):
            print 'code:', r.status_code
            #convert json to python form
            data = json.loads(r.text or r.content)
            #print type(data) #dic
            #JSON form
            json_out = json.dumps(data, sort_keys=True, indent=4)
            print '-----'*10, 'JSON OUT', '-----'*10
            print json_out
            print '-----'*10, 'JSON END', '-----'*10
        else:
            print "Error: Unreachable to the host", 'url'
            print 'code:', r.status_code


