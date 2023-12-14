from bs4 import BeautifulSoup
from selenium import webdriver

def extract_wanted(keyword):
    base_url="https://www.wanted.co.kr/search?query="
    browser = webdriver.Chrome()
    browser.get(f"{base_url}{keyword}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    jobs = soup.find("div", {"role": "list"})
    job = jobs.find_all("div", {"role": "listitem"})
    result = []
    for item in job:
        anchor = item.select_one("a")
        title = item.find("strong", class_="JobCard_title__ddkwM")
        company = item.find("span", class_="JobCard_companyName__vZMqJ")
        region = item.find("span", class_="JobCard_location__2EOr5")
        link = anchor['href']
        job_data = {
            'title' : title.string.replace(",", " "),
            'company' : company.string.replace(",", " "),
            'region' : region.string.replace(",", " "),
            "link" : f"https://www.wanted.co.kr{link}"
        }
        result.append(job_data)
    return result

