#! python3
## updatedhomeIP.py - alert when home Public IP changes

import requests, os, urllib3, re
from emailTool import sendMail
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

## get ipv4 addr
ipaddr = requests.get('http://ipinfo.io/ip', verify=False).text

## directory and env etup
base_dir = os.path.dirname(__file__)
os.chdir(base_dir)
config_dir = 'config'
os.makedirs(config_dir, exist_ok=True)
os.chdir(config_dir)
load_dotenv('.env')

### email configs
mailusr = 'alerts.digga@gmail.com'
mailpw = os.getenv('mailpw')
sender = 'Ed Reyes <alerts.digga@gmail.com>'
receivers = ['eggadigga19@gmail.com']
cc = ['egga19@yahoo.com', 'eduardo.reyes120@gmail.com']
server = 'smtp.gmail.com'

### txt file with IP
fname = 'ipv4.txt'
if os.path.exists(fname) == False:
    ipFile = open(fname, 'w')
    ipFile.write('172.0.0.1 - placeholder')
    ipFile.close

ipFile = open(fname, 'r')
for line in ipFile:
    if line not in ipaddr:
        open(fname, 'w').write(ipaddr)
        sub = 'EP Home IP Change'
        body = 'IP is now: ' + ipaddr
        sendMail(sender, receivers, cc, sub, body, mailusr, mailpw, server)
    else:
        continue
ipFile.close()
