from lxml import html
import requests
import re
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
pics=list()
def instadp(a,username,b):
    raw_html_code = requests.get('https://www.instagram.com/'+username+'/?hl=en" hreflang="en"')
    html_code=raw_html_code.content
    html_code=BeautifulSoup(html_code,'lxml')
    script_tag=html_code.find_all('script')[a]
    links=re.finditer('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',script_tag.text)
    for i in links:
        pics.append(i.group())
    response = requests.get(pics[b])
    img = Image.open(BytesIO(response.content))
    img.show()
username=input("Enter Insta Username: ")
try:
    instadp(4,username,1)
except OSError:
    instadp(4,username,3)
except IndexError:
    try:
        instadp(3,username,1)
    except OSError:
        instadp(3,username,3)
    except:
        print("Invalid username")