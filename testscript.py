import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
protocols = ["https","http"]
with open('test.json')as f:
	data = json.load(f)
print data.keys()
print data.values()
for key,value in data.iteritems():
	print key
	for website in value:
		for proto in protocols:
			response = requests.get(proto + "://" + website, verify=False)
			print proto + "://" + website,response.status_code





