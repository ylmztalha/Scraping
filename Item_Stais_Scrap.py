import requests
from bs4 import BeautifulSoup as bs
import base64
import json

headers = {
    'authority': 'www.itemsatis.com',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.itemsatis.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.itemsatis.com/favori-ilanlarim.html',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '__cfduid=de5c49921aed930d589650b268446305f1613733981; _gid=GA1.2.786510391.1613733991; __tawkuuid=e::itemsatis.com::9Zh7no2t2fL+E7KxfdlDmhH0i9xkmbtl2I8MtogHbtbgJrROZCJIiXHKhUohxULf::2; PHPSESSID=h2c2q55hknpves35235ocgepe3; _ga_ZN0SH1X916=GS1.1.1613744373.2.1.1613744545.0; _ga=GA1.2.1069633345.1613733991; _gat_gtag_UA_162782217_2=1; TawkConnectionTime=0',
}

data = {
  'UserName': 'ylmztalha',
  'Password': 'S4league',
  'csrf_token': 'a6fdd1c0767170800fde78cf70b41806'
}
s=requests.session()

response = s.post('https://www.itemsatis.com/api/Login', headers=headers, data=data)

r=s.get('https://www.itemsatis.com/favori-ilanlarim.html',headers=headers)

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
    x=zip(liste_h,liste5)
    liste6.append(tuple(x))

json_n = json.dumps(liste6)


with open("scrap_j.json", "w") as write_file:
    json.dump(json_n, write_file)



