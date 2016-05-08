import requests
import io

from bs4 import BeautifulSoup
##beautifulsoup import
Murl = "http://www.melon.com/chart/month/index.htm#params%5Bidx%5D=1&params%5BrankMonth%5D=201604&params%5BisFirstDate%5D=false&params%5BisLastDate%5D=true"
##bringing this webpage
rq = requests.get(Murl)	##get this webpage
Msoup = BeautifulSoup(rq.content)

test_data = Msoup.find_all("div", {"class": "wrap_song_info"})


with io.open('log.txt','a', encoding='utf8') as logfile:
	for item3 in test_data:
		try:
			print item3.find_all("strong",)[0].text 
			print item3.find_all("span",{"class": "checkEllipsis"})[0].text
			
			logfile.write(u"%s ,  %s  \n" % (item3.find_all("strong",)[0].text,item3.find_all("span",{"class": "checkEllipsis"})[0].text))
		except:
			pass
	logfile.close()

		
		
		##logfile.write(u"%s \n\n" % (item3.find_all("span",{"class": "checkEllipsis"})[0].text))

##print item3.find_all("div",{"class": "ellipsis rank03"})[0].text
"""
for item1 in title_data:
	try:
		print item1.contents[0].text			
	except:
		pass

for item2 in singer_data:
	try:
		print item2.contents[0].text
	except:
		pass
"""




"""
url = "http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles%2C+CA"
url_page_2 = url
	  "http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los%20Angeles%2C%20CA&page=2"
r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")

for link in links:
##	if "http" in link.get("href"): ## only get href link not nonetype
	print"<a href='%s'>%s</a>" %(link.get("href"), link.text)

g_data = soup.find_all("div",{"class": "info"})
for item in g_data:
	print item.contents[0].find_all("a",{"class": "business-name"})[0].text
	print item.contents[1].text
	try:
		print item.contents[1].find_all("p",{"class": "body with-avatar"}).text
	except:
		pass

"""


