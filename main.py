from bs4 import BeautifulSoup
from selenium import webdriver

def get_page_count(keyword):
    browser = webdriver.Chrome()
    base_url="https://kr.indeed.com/jobs?q="
    browser.get(f"{base_url}{keyword}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("ul", class_="css-1g90gv6 eu4oa1w0") 
    if pages == None:
        return 1
    else:
        pages = pagination.find_all("li", recursive=False) #recursive의 기능 : ul바로 아래 있는 li만을 검색 . li의 li까지 검색하고 싶지 않을 때
        count = len(pages)
        if count >= 5:
            return 5
        else:
            return count 
        
def extract_indeed(keyword):
    pages = get_page_count(keyword)
    for page in range(pages):
        browser = webdriver.Chrome() #import webdriver -> browser = webdriver.Chrome() -> browser.get("URL")
        base_url="https://kr.indeed.com/jobs?q="
        browser.get(f"{base_url}{keyword}")
        soup = BeautifulSoup(browser.page_source, "html.parser") #browser.page_source는 response.text를 대신해주며, 웹페이지의 HTML을 긁어와준다.
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
                        'title': title.string, #.string은 긁어온 HTML에서 글자만 뽑아준다.
                        'company': company.string,
                        'region': region.string,
                        'link': f"http://kr.indeed.com{link}"
                    }
                    result.append(job_data)
    return result
            


while (True): #창이 잠깐 켜졌다 꺼지는 오류를 해결 
    pass