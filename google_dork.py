# doing a google research of all the urls in a page
import requests
from bs4 import BeautifulSoup
from header_parser import headers_parser
import re

class Google:
	def __init__(self):
		self.headers = headers_parser(headers)
		self.url = "https://www.google.com/search"
		self.emails = []

	def search(self):
		text = input("Enter Keyword: ")
		pages = input("How many pages?")
		start = 0
		for i in range(int(pages)):
			print(f"Page number {i+1}")
			print(self.google_search(text, str(start)))
			start = int(start) + 10

	def extract_links(self, html):
		soup = BeautifulSoup(html, 'html.parser')
		for link in soup.select('.r a:not([class])'):
			res = requests.get(link['href'])
			email = re.findall('[a-zA-Z0-9_.+-]+@intel.com', res.text)
			self.emails.append(email)
			print(email)

	def google_search(self, text, start='0'):
		newparams = {
			'q': text,
			'oq': text,
			'start': start
		}
		response = requests.get(self.url, params=newparams, headers=headers_parser(headers))
		self.extract_links(response.text)


headers = '''Host: www.google.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Referer: https://www.google.com/
Cookie: CGIC=Ij90ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSwqLyo7cT0wLjg; NID=197=E-4YOt-eDGaujR68iLrzNVD1PhmVWpjLEQF7jUMq4f-Xkx>
Connection: keep-alive'''

search = Google()
search.search()
