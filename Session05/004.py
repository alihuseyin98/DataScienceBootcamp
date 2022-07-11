import requests
from bs4 import BeautifulSoup
response=requests.get('https://www.usatoday.com/news/')
soup=BeautifulSoup(response.text)
#main_links=['https://www.usatoday.com'+c['href'] for c in soup.find_all('a',{'class':'gnt_n_mn_l'})]
main_links=['https://www.usatoday.com'+c['href'] for c in soup.find_all('a',{'class':'gnt_n_mn_l'})]
articles=[]
#print(main_links[:5])
for ml in main_links[:5]:
    print(ml)
    response=requests.get(ml)
    print(response)
    soup=BeautifulSoup(response.text)
    links=['https://www.usatoday.com'+c['href'] for c in soup.find_all('a',{'class':'gnt_m_th_a'})]
    #print(links)
    for l in links:
        response=requests.get(l)
        soup=BeautifulSoup(response.text)
        
        try:
           print(soup.find('a',{'class':'gnt_ar_lbl_a'}).get_text())
        except:
            print("NONE")
        
        
    #print([soup.get_text()])
print("+++++++++++++++")

    