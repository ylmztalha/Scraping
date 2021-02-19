import requests
from bs4 import BeautifulSoup as bs

Login_url="https://www.itemsatis.com/api/Login"

fav_ilan="https://www.itemsatis.com/favori-ilanlarim.html"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }


s=requests.session()

payload = {"UserName":"ylmztalha","Password":"S4league","csrf_token": "e89303e64f1b9b10fa39795c35f33aba"}


login_req = s.post(Login_url,headers=headers,data=payload)



soup = bs(s.get(fav_ilan).text,'html.parser')

