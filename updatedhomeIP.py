#! python3
## updatedhomeIP.py - alert when Public IP changes

from doctest import NORMALIZE_WHITESPACE
import requests, os, urllib3, re
from bs4 import BeautifulSoup
from emailTool import sendMail

os.makedirs(r'c:\temp', exist_ok=True)
os.chdir(r'c:\temp')

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

resp = requests.get('https://www.iplocation.net/find-ip-address', verify=False)
soup = BeautifulSoup(resp.text, 'html.parser')

fname = 'IP-check.txt'
if os.path.exists(fname) == False:
    ipFile = open(fname, 'w')
    ipFile.write('172.0.0.1 - placeholder')
    ipFile.close

ipFile = open(fname, 'r')
for ip in soup.strings:
   if 'IPv4' in repr(ip):
       print(ip)
       for line in ipFile:
           if line not in ip:
               ipOnly = re.compile('\d+.*').findall(ip)[0]
               open(fname, 'w').write(ipOnly)
               emailSub = 'Eggadigga IP Has Changed'
               sendMail(emailSub,ip)
   else:
       continue

ipFile.close()
