import urllib3
from bs4 import BeautifulSoup
import re

http = urllib3.PoolManager()

data = []

# specify the url
quote_page = 'https://offthegrid.com/event/salesforce-transit-center/2020-1-16-11AM'
print (quote_page)

# query the website and return the html to the variable ‘page’
response = http.request('GET', quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(response.data.decode('utf-8'), features="lxml")

# Take out the <div> of name and get its value
name_box = soup.findAll('a', attrs={'href': re.compile("^https://offthegrid.com/creator")})
print (name_box)