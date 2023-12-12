from requests import get
from bs4 import BeautifulSoup

base_url="https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term="python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
    print("Nooooo!!!")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("section", class_="jobs") #jobs는 List이다.
    for job_section in jobs:
        job_posts = job_section.find_all("li")
        for post in job_posts:
            if 'view-all' not in post.get('class', []): 
                #post로 가져온 클래스 리스트에 view-all이 없는 경우 True가 되는 조건문
                #post.get('class', [])는 post 엘리먼트의 'class'속성 값을 가져옴. 
                # 그리고 만약 속성 값이 존재하지 않으면 빈 []를 반환
                print("//////////")
                print(post)