#!/usr/bin/env python
# coding:utf-8

import re
import requests
from bs4 import BeautifulSoup
import json


#monitorUrl = 'https://xxxx/sp/sp_main.php'
cliUrl = 'https://xxxx/sp/sp_maint/spm_docli_cmd.php?mode=show&cluster=SS7400&clicmd='
command = 'showpd -showcols Id,CagePos -nohdtot'
username = 'xxxx'
password = 'xxxx'
data = list()

#r = requests.get(monitorUrl, auth=(username, password), allow_redirects=False, verify=False)
#sessionID = r.headers['set-cookie'].split(';')[0]
#print sessionID
s = requests.Session()
r = s.get(cliUrl+command, auth=(username, password), verify=False)
soup = BeautifulSoup(r.text)
result = soup.find_all('pre')[1].text
#print result
splitPat = re.compile(r'\s+')
for line in result.split('\n'):
    stripLine = line.strip()
    if stripLine:
        lineList = splitPat.split(stripLine)
        #print lineList
        data.append({"{#PDID}":lineList[0], "{#PDCAGE}":lineList[1]})
print(json.dumps({"data": data}, indent=4))