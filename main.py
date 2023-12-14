from extractors.indeed import extract_indeed
from extractors.wwr import extract_wwr
from selenium import webdriver

keyword = input("What are you searching for jobs?")

indeed = extract_indeed(keyword)
wwr = extract_wwr(keyword)
jobs = indeed + wwr #리스트끼리 합칠 수 있다
print(jobs)

while (True): #창이 잠깐 켜졌다 꺼지는 오류를 해결 
    pass