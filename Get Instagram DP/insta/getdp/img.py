from lxml import html
import requests
import re
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
pics=list()
class getimg:
	def __init__(self):
		pass
	def calling(username):
		try:
			return instadp(4,username,1)
		except OSError:
			return instadp(4,username,3)
		except IndexError:
			try:
				return instadp(3,username,1)
			except OSError:
				return instadp(3,username,3)
			except:
				return "https://us.123rf.com/450wm/chrisdorney/chrisdorney1411/chrisdorney141100155/34073570-invalid-red-rubber-stamp-over-a-white-background-.jpg?ver=6"

def instadp(a,username,b):
	pics=list()
	raw_html_code = requests.get('https://www.instagram.com/'+username+'/?hl=en" hreflang="en"')
	html_code=raw_html_code.content
	html_code=BeautifulSoup(html_code,'lxml')
	script_tag=html_code.find_all('script')[a]
	links=re.finditer('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',script_tag.text)
	for i in links:
		pics.append(i.group())
	return pics[b]

