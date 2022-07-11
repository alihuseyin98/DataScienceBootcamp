import requests
from datetime import date
from  bs4 import BeautifulSoup
response=requests.get('https://www.bbc.com/')
soup=BeautifulSoup(response.text)
headlines=[l.get_text().strip() for l in soup.find_all('a',{'class':'media__link'})]
today = date.today()
print(today.isocalendar())
d=str(today.day)
print(d)