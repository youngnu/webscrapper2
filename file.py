def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w")
    file.write("Title, Company, Location, Url\n") #file.write()는 하나의 argument만을 받는다.

    for job in jobs:
        file.write(f"{job['title']},{job['company']},{job['region']},{job['link']}\n")

    file.close()
