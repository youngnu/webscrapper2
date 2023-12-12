from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome() #import webdriver -> browser = webdriver.Chrome() -> browser.get("URL")
base_url="https://kr.indeed.com/jobs?q="
search_term="python"
browser.get(f"{base_url}{search_term}")

while (True): #창이 잠깐 켜졌다 꺼지는 오류를 해결 
    pass