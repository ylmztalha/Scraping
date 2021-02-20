import requests
from bs4 import BeautifulSoup as bs
import lxml
import base64
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
}
log_url="https://www.itemsatis.com/api/Login"

url="https://www.itemsatis.com"

url2="https://www.itemsatis.com/favori-ilanlarim.html"

s = requests.session()
r = s.get(url)
soup = bs(r.text,'lxml')

csrf_token = soup.find('input',{'name':'csrf_token'})['value']
cookies = r.cookies

headers['X-CSRF-Token'] = csrf_token
headers['X-Requested-With'] = 'XMLHttpRequest'

payload = {
    'UserName': 'ylmztalha',
    'Password': 'S4league',
    'remember':'1'
}
r = s.post(log_url, cookies=cookies, data=payload, headers=headers)
r = s.get(url2)

soup = bs(r.text,'html.parser')

fiyat =soup.find_all('div',{'class':'AdvertBox-Price'})
liste=[]
for i in fiyat:
    liste.append(i.get_text())


img2 = soup.find_all('img')
liste2=[]
for i in img2:
    if i.get('data-src')is None:
        pass
    else:
        liste2.append(i.get('data-src'))

link2=soup.find_all('div',{'class':'col-md-4 col-sm-12 col-xs-12 AdvertBox-1'})
liste3=[]
for i in link2:
    liste3.append(i.find('a').get('href'))


liste4=[]
for i in liste2:
    bs=base64.b64encode(requests.get(i).content)
    ds=bs.decode("utf-8")
    liste4.append(ds)


liste_h=["Link","Fiyat","Resim Link","Base64"]

liste6=[]
for i in range(0,3):
    liste5=[]
    liste5.append(liste3[i])
    liste5.append(liste[i])
    liste5.append(liste2[i])
    liste5.append(liste4[i])
    x=dict(zip(liste_h,liste5))
    liste6.append(x)

with open("scrap_j2.json", "w") as write_file:
    json.dump(liste6, write_file)

