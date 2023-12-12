from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome() #import webdriver -> browser = webdriver.Chrome() -> browser.get("URL")
base_url="https://kr.indeed.com/jobs?q="
search_term="python"
browser.get(f"{base_url}{search_term}")
soup = BeautifulSoup(browser.page_source, "html.parser")
div = soup.find_all("div", {'id': 'mosaic-jobResults'})
for job_result in div:
    ul = job_result.find("ul", class_="css-zu9cdh eu4oa1w0") #find_all 다음에 find_all을 쓰면 안되는가?
    for li in ul:
        mosaic_zone = li.find("div", class_="mosaic-zone")
        if mosaic_zone == None:
            anchor = li.select_one("h2 a")
            link = anchor["href"]
            title = li.select_one("h2 a span")
            company = li.find("span", {"data-testid": "company-name"})
            region = li.find("div", {"data-testid": "text-location"})
            print(title, company, region)
            
        

while (True): #창이 잠깐 켜졌다 꺼지는 오류를 해결 
    pass