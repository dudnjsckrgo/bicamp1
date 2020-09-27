import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from crawler.chromehandler import ChromeDriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import re
from urllib.request import urlopen
from crawler.service import  Service
from crawler.entity import  Entity


class ChromeListener:
    def __init__(self):
        self.driver = ChromeDriver()
        self.bs4Sel = Bs4Sel()
        self.service = Service()
        self.entity = Entity()
    def searching_data(self,si):
        driver= self.driver
        driver.si = si
        driver=ChromeListener.get_sichug_url(driver)
        driver=ChromeListener.get_corona_page(driver)



class Bs4Sel(Service):
    def __init(self):
        self.driver = ChromeDriver()
        self.service = Service()
        self.entity= Entity()
    @staticmethod
    def get_sichug_url(driver):
    # 정부24의 정부/지자체 운영사이트에서 검색해서 들어감
        url = driver.jungbu
        spyder = driver.spyder
        si = driver.si
        
        spyder.get(url)
        x = spyder.find_element_by_xpath('//*[@id="srchTxt"]')
        ActionChains(spyder).move_to_element(x).send_keys(si,Keys.ENTER).perform()
        #/html/body/div/div[3]/div/div/div/div[2]/ul/li[1]/dl/dt/a
        #/html/body/div/div[3]/div/div/div/div[2]/ul/li[2]/dl/dt/a
        try:
            for x in spyder.find_elements_by_xpath('/html/body/div/div[3]/div/div/div/div[2]/ul/'):
                print(x)
                
                if re.search(si,x.text) != None:
                    for i in x.text.split(' '):
                        if re.match(si, i) != None:
                            pass
                else:
                    pass

            
        return driver
    @staticmethod
    def get_corona_page(driver):
        return driver
    @staticmethod
    def find_patten(driver):
        pass
    
    

if __name__ == "__main__":
    
    print('1, 동대문구')
    print('2, 수원')
    x = input('어느 지역에 사시나요?')
    if x== '1':
        si = "동대문구"
    elif x== '2':
        si = '수원'
    api = ChromeListener()
    api.searching_data(si)

