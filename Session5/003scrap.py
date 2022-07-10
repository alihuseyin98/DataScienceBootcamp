from turtle import pen
import requests
import re
from bs4 import BeautifulSoup
res=requests.get("https://www.bbc.com/")                        #----------------
soup=BeautifulSoup(res.text)                                    #----------------
print(type(soup))
#print(soup)
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++\n")
#childs=(soup.children) #<class 'list_iterator'> but not list #----------------
"""i=iter(soup.children)
print("-",i)
print("-",next(i))
print("-",next(i))
print("-",next(i))
print("-",next(i))"""
#print("-",list(childs[3])[3])
#print(soup.get_text())                                          #----------------
#print(re.findall("\w+\s?\w*",soup.get_text()))
#print(soup.find_all(_class='module__title__link tag tag--news'))
#print(soup.find_all('h3')[0])
#print("\n++++++ ",soup.get_text())
#print("\n++++++ ",soup.find_all('h3',{'class':'media__title'}))  # return h3 that has ... #----------------
#print("\n++++++ ",re.findall("'I've taught my mum some things about finance'",[x.get_text().strip() for x in (soup.find_all('h3',{'class':'media__title'}))]))
#print("\n++++++ ","over a family for 41 years" in [x.get_text().strip() for x in (soup.find_all('h3',{'class':'media__title'}))])
#print("\n++++++ ",soup.find_all('h3',{'class':'media__title'})[-1].get_text().strip())
#print("\n++++++ ",soup.find_all('a',{'class':'media__link'})[0].get_text().strip())
# MESSİON FİND ALL CLASS OF h3 İN THE SİTE