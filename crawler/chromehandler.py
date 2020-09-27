from dataclasses import dataclass
from selenium import webdriver
@dataclass
class ChromeDriver:
    spyder :object = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
    jungbu : str = 'https://www.gov.kr/portal/orgSite?'
    si : str = ''
    
