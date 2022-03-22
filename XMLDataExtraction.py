import xml.etree.ElementTree as ET
import ssl
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1481947.xml"
xml = urllib.request.urlopen(url, context=ctx).read().decode()

tree = ET.fromstring(xml)
lst = tree.findall('.//count')
s = 0  # Sum of all numbers
for item in lst:
    s += int(item.text)

print(f"Sum = {s}")
