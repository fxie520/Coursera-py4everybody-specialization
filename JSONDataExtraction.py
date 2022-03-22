import json
import ssl
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1481948.json"
js = urllib.request.urlopen(url, context=ctx).read().decode()
js = json.loads(js)

s = 0  # Sum of all numbers
comments = js["comments"]
for comment in comments:
    s += comment["count"]

print(f"Sum is {s}")
