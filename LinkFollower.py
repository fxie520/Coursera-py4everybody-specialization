import re
import ssl
import urllib.request

from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Asha.html"
html = urllib.request.urlopen(url, context=ctx).read().decode()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags
repeat = 7
position = 18
names = []
urls = []
for _ in range(repeat):
    tag = soup('a')[position - 1]
    names.append(tag.contents[0])
    url = re.findall('href="(.+)"', str(tag))[0]
    urls.append(url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

print(f"Names: {names}")
print(f"Urls: {urls}")
