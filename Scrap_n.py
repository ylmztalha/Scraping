from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

browser = webdriver.Chrome()
browser.get('https://www.itemsatis.com/index.php')

giriş = browser.find_elements_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul[2]/li')
giriş[0].click()

user_n=browser.find_elements_by_xpath('//*[@id="loginForm"]/div[1]/input')
user_p=browser.find_elements_by_xpath('//*[@id="loginForm"]/div[2]/input')

user_n[1].send_keys("ylmztalha")
user_p[1].send_keys("S4league")

log_in=browser.find_elements_by_xpath('//*[@id="loginForm"]/button')
log_in[1].click()

browser.get('https://www.itemsatis.com/favori-ilanlarim.html')

fiyat_n=browser.find_elements_by_xpath('/html/body/section/div/div/div/div[*]/div/div[1]')
link_n=browser.find_elements_by_xpath('/html/body/section/div/div/div/div[*]/div/a[1]')
resim_n=browser.find_elements_by_xpath('/html/body/section/div/div/div/div[*]/div/a[1]/img')

liste_h=("Link","Fiyat","Resim Link")

liste_n=[]
for i in range(0,len(fiyat_n)):
    liste_n2=[]
    liste_n2.append(link_n[i].get_attribute('href'))
    liste_n2.append(fiyat_n[i].text)
    liste_n2.append(resim_n[i].get_attribute('src'))
    x= zip(liste_h,liste_n2)
    liste_n.append(tuple(x))

json_l=[]
for i in liste_n:
    xx=dict(i)
    json_l.append(xx)

jsonString = json.dumps(json_l)

with open("data_file.json", "w") as write_file:
    json.dump(jsonString, write_file)


