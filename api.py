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


    def send(self, url, payload):
        print '==========Sending Request=========='
        print '[POST]'
        print '(' + url + ')'
        
        data=json.dumps(payload)
        r = requests.post(url, data)
        
        print '-----'*10, 'INPUT DATA', '-----'*10
        print r.text
        print '-----'*10, 'INPUT END', '-----'*10
        
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





#    def RepoNames(self, url):
#        r = requests.get(url)
#        if (r.ok):
#            data = json.loads(r.text or r.content)
#            print '==========List of the Repos=========='
#            print '(' + url + ')'
#            json_out = json.dumps(data, sort_keys=True, indent=4)
#            #for i in range(0, len(data)):
#                #print data[i]['name']
#            print json_out
#        else:
#            print "Error: Unreachable to the host", 'url'
#            sys.exit()
#
#    def totalNumberOfRepos(self, url):
#        r = requests.get(url)
#        if (r.ok):
#            data = json.loads(r.text or r.content)
#            print 'Total number of Repo: ' + '[' + str(len(data)) + ']'
#
#    def send(self, url):
#        r = requests.post(url)
#        ir
#url = 'https://api.github.com/users/chasiumen/repos'
#a = git_api('test')
#a.RepoNames(url)
#a.totalNumberOfRepos(url)
