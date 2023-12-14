from extractors.indeed import extract_indeed
from extractors.wwr import extract_wwr

keyword = input("What are you searching for jobs?")
'''
indeed = extract_indeed(keyword)
wwr = extract_wwr(keyword)
jobs = indeed + wwr #리스트끼리 합칠 수 있다
'''
file = open(f"{keyword}.csv", "w")
file.write("Title, Company, Location, Url\n") #file.write()는 하나의 argument만을 받는다.
file.close()

