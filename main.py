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
    result = []
    for job_section in jobs:
        job_posts = job_section.find_all("li")
        for post in job_posts:
            if 'view-all' not in post.get('class', []): 
                #post로 가져온 클래스 리스트에 view-all이 없는 경우 True가 되는 조건문
                #post.get('class', [])는 post 엘리먼트의 'class'속성 값을 가져옴. 
                # 그리고 만약 속성 값이 존재하지 않으면 빈 []를 반환
                anchors = post.find_all('a')
                anchor = anchors[1] #anchors List에서 두번째 "a"를 찾아주는 방법 
                link = anchor['href'] # link 변수에 anchor의 href를 전달하는 방식 list나 dictionary에서 주로 쓰이는 방식
                company, time, region = anchor.find_all("span", class_="company")
                #[] list의 각 값에 변수를 할당하는 방법
                title = anchor.find("span", class_="title")
                # find_all은 list를 반환하지만, find는 결과를 가져온다. BeautifulSoup의 기능!
                job_data = {
                    'title': title.string,
                    'company': company.string,
                    'time': time.string,
                    'region': region.string
                }
                result.append(job_data) #list에 dictionary 값을 넣는 방법 list.append(dictionary)
    print(result) # for loop 밖에 result를 정의함으로써 data를 저장