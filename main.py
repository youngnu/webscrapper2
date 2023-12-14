from extractors.indeed import extract_indeed
from extractors.wwr import extract_wwr

keyword = input("What are you searching for jobs?")

indeed = extract_indeed(keyword)
print(indeed)

