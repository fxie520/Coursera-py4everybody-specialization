import json
import ssl
import urllib.parse
import urllib.request

api_key = 42
service_url = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = "University of Washington - Bothell"
if len(address) < 1:
    raise ValueError

params = dict()
params['address'] = address
params['key'] = api_key
url = service_url + urllib.parse.urlencode(params)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

js = json.loads(data)

place_id = js['results'][0]['place_id']
print(f"Place id is {place_id}")
