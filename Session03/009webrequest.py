import requests
res1= requests.get("https://raw.githubusercontent.com/homsit/files/main/invdata2.txt")
res2=requests.get("https://raw.githubusercontent.com/homsit/files/main/invdata1.txt")
print(res1.text)
print(res2)
