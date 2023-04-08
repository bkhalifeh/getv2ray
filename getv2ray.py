import requests
import base64
import json
import os
import re
servers = []
if not os.path.isfile('last_server.json'):
	with open('last_server.json', 'w') as f:
		f.write('[]')

last_server = json.loads(open('last_server.json', 'r').read())

outs = open('v2ray-servers.txt', 'wb')

def isNotSSR(c):
	return not c.startswith('ssr')

def getTextFromUrl(u):
	return requests.get(u).text

def getServerFromBase64(s):
	for j in s.splitlines():
		for i in base64.b64decode(j.strip()).decode().splitlines():
			if isNotSSR(i):
				servers.append(i)


def getServerFromUrl(u):
	for i in getTextFromUrl(u).splitlines():
		if isNotSSR(i.strip()):
			servers.append(i)

def getServerWithPattern(u):	
	servers.extend(re.findall(r'(vmess|vless|trojan|ss)://.+', getTextFromUrl(u)))


simple_urls = [
	'https://raw.githubusercontent.com/learnhard-cn/free_proxy_ss/main/free',
	'https://raw.githubusercontent.com/mfuu/v2ray/master/v2ray',
	'https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub',
	'https://raw.githubusercontent.com/tbbatbb/Proxy/master/dist/v2ray.config.txt',
	'https://raw.githubusercontent.com/freefq/free/master/v2',
	'https://raw.githubusercontent.com/Leon406/SubCrawler/main/sub/share/all2',
	'https://raw.githubusercontent.com/openRunner/clash-freenode/main/v2ray.txt',
	'https://raw.githubusercontent.com/Jsnzkpg/Jsnzkpg/Jsnzkpg/Jsnzkpg',
	'https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2',
	'https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.txt',
	'https://raw.githubusercontent.com/openRunner/clash-freenode/main/v2ray.txt',
	'https://raw.githubusercontent.com/vpei/Free-Node-Merge/main/o/node.txt',
	'https://raw.githubusercontent.com/ermaozi01/free_clash_vpn/main/subscribe/v2ray.txt',
	'https://raw.githubusercontent.com/ripaojiedian/freenode/main/sub'
]

spl_urls = [
	'https://raw.githubusercontent.com/HakurouKen/free-node/main/public',
	'https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/configs.txt'
]

re_urls = [
	'https://raw.githubusercontent.com/tolinkshare/freenode/main/README.md',
	'https://raw.githubusercontent.com/mianfeifq/share/main/README.md'
]

for su in simple_urls:
	getServerFromBase64(getTextFromUrl(su))

for su in spl_urls:
	getServerFromUrl(su)

for ru in re_urls:
	getServerWithPattern(ru)



servers = list(set(servers))
for server in servers:
	if server not in last_server:
		last_server.append(server)
		outs.write((server + '\n').encode())
outs.close()

uls = open('last_server.json', 'w')
uls.write(json.dumps(last_server))
uls.close()