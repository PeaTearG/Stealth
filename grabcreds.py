import os
import json


def importcredjson(path=True):
    if path:
        path = 'C:\\Users\\Administrator\\PycharmProjects\\Credentials\\creds.json'
    else:
        currpath = os.path.abspath("")
        dirname = os.path.dirname(currpath)
        creddir = "\\Credentials\\creds.json"
        path = dirname + creddir
    f = open(path, mode="r")
    return json.loads(f.read())

def grabcred(credjson,service,instance):
   for i in credjson[service]:
       if i['instance'] == instance:
           return i['username'], i['password'], i['fqdn']
       else:
           pass

def main(service, instance, path=None):
    credjson = importcredjson()
    u,p,d = grabcred(credjson,service,instance)
    return u,p,d

