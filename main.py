from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome() #import webdriver -> browser = webdriver.Chrome() -> browser.get("URL")
base_url="https://kr.indeed.com/jobs?q="
search_term="python"
browser.get(f"{base_url}{search_term}")
soup = BeautifulSoup(browser.page_source, "html.parser")
div = soup.find_all("div", {'id': 'mosaic-jobResults'}) #{}형태로 찾아줄수도있다.
result = []
for job_result in div:
    ul = job_result.find("ul", class_="css-zu9cdh eu4oa1w0") #find_all 다음에 find_all을 쓰면 안되는가?
    for li in ul:
        mosaic_zone = li.find("div", class_="mosaic-zone") # class로 mosaic-zone을 가지고 있는 div는 필터링
        if mosaic_zone == None:
            anchor = li.select_one("h2 a")
            link = anchor["href"]
            title = li.select_one("h2 a span")
            company = li.find("span", {"data-testid": "company-name"})
            region = li.find("div", {"data-testid": "text-location"})
            job_data = {
                'title': title.string,
                'company': company.string,
                'region': region.string,
                'link': f"http://kr.indeed.com{link}"
            }
            result.append(job_data)
print(result)
            
        

while (True): #창이 잠깐 켜졌다 꺼지는 오류를 해결 
    pass