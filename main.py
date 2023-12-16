from extractors.indeed import extract_indeed
from extractors.wwr import extract_wwr
from extractors.wanted import extract_wanted
from file import save_to_file

keyword = input("What are you searching for jobs?")

indeed = extract_indeed(keyword)
wwr = extract_wwr(keyword)
wanted = extract_wanted(keyword)
jobs = indeed + wwr + wanted #리스트끼리 합칠 수 있다

save_to_file(keyword, jobs)