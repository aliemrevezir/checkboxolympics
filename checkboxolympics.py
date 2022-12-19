import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
r = requests.get("https://checkboxolympics.com")
driver_path = "Masaüstü\chromedriver.exe"
browser = webdriver.Chrome(driver_path)
browser.get("https://checkboxolympics.com/")
ready = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[2]/button')
ready.click()
sayfa_kaynagi = browser.page_source
sayfa = BeautifulSoup(sayfa_kaynagi, "html.parser")
zaman = sayfa.find("div", attrs={"class":"time"}).text.lstrip("Time: ")
while type(zaman) == str:
    sayfa_kaynagi = browser.page_source
    sayfa = BeautifulSoup(sayfa_kaynagi, "html.parser")
    zaman = (sayfa.find("div", attrs={"class":"time"}).text.lstrip("Time: "))
    try:
        zaman = float(zaman)
    except ValueError:
        continue
    if type(zaman) != float:
        while type(zaman)!=float:
            print(zaman)
            zaman = float(sayfa.find("div", attrs={"class":"time"}).text.lstrip("Time: "))
    if type(zaman) == float:
        break
if type(zaman) == float:
    for i in range(1,29):
                
        kutular = browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/input[{}]'.format(i))
        kutular.click()
i=0
while i<1:
    continue
    
