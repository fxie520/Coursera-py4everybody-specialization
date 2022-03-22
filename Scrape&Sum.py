from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1481945.html"
html = urlopen(url, context=ctx).read().decode()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all the anchor tags
s = 0  # Sum of all numbers
tags = soup('span')
for tag in tags:
    s += int(tag.contents[0])
print(f"Sum is {s}")
