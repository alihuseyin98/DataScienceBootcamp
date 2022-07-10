from turtle import pen
import requests
import re
from bs4 import BeautifulSoup
res=requests.get("https://www.instagram.com/yildiz_arabic_family/followers/")                        #----------------
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
print("\n++++++ ",soup.find_all('a',{"class":"_aacl _aaco _aacw _aacx _aad7 _aade"}))