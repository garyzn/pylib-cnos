import requests
import json
# Utility Functions

def form_url(conn, url):
   url = conn.transport+'://' + conn.ip + ':' + conn.port + url
   return url

def form_hdr(conn):
   hdr = dict()
   tmp_ckie = 'auth_cookie='+conn.cookie + ';user='+ conn.user +'; Max-Age=3600; Path=/'
   hdr['Cookie'] = tmp_ckie
   hdr['Content-type'] = 'application/json'
   return hdr

class Connection:
     def __init__(self,params):
         self.transport = params['transport']
         self.port = params['port']
         self.ip = params['ip']
         self.user = params['user']
         self.password = params['password']
         self.cookie = ''
         self.url = self.transport + '://' + self.ip + ':' + self.port
#         print(self.url, self.user, self.password)

         # Step 1 - Login and get the auth cookie
         ret = requests.get(self.url + '/nos/api/login/',auth=(self.user, self.password),verify=False, timeout=20)
         self.cookie=ret.cookies['auth_cookie']
#         print(self.cookie)

         # Step 2 - Login with valid cookie
         tmp_ckie = 'auth_cookie=' + self.cookie + ';user='+ self.user +'; Max-Age=3600; Path=/'
         self.hdr=dict()
         self.hdr['Cookie']=tmp_ckie

         ret = requests.get(self.url + '/nos/api/login/', headers=self.hdr, auth=(self.user, self.password),verify=False)
         self.cookie=ret.cookies['auth_cookie']
#         print(self.cookie)
         self.hdr['Cookie'] = 'auth_cookie=' + self.cookie + ';user='+ self.user +'; Max-Age=3600; Path=/'
         self.hdr['Content-Type']='application/json'

     def get(self, url):
         ret = requests.get(self.url + url, headers=self.hdr, auth=(self.user, self.password),verify=False)
         if (ret.status_code == 200):
            return (1, ret.json()) 
         return (0, ret.status_code) 

     def put(self, url, inp):
         ret = requests.put((self.url + url), data=json.dumps(inp), headers=self.hdr, auth=(self.user, self.password),verify=False)
         return ret

     def post(self, url, inp):
         ret = requests.post((self.url + url), data=json.dumps(inp), headers=self.hdr, auth=(self.user, self.password),verify=False)
         print ret.status_code
         if (ret.status_code == 200):
            return (1, ret.json()) 
         return (0, ret.status_code) 

