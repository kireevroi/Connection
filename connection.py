import csv
import requests

list_status = []
list_status.append(["Website", "Working"])

def scrape():
    with open("websites.txt", "r") as inquiry:
        for i in inquiry:
            website = i.strip()
            status = requests.get(website).status_code
            print(status)
            if status == 200:
                list_status.append([website, "Working"])
            else:
                list_status.append([website, "Not Working"])
    return list_status

def export(export_list):
    with open("status.csv", "w", newline = "") as export_write:
        writing = csv.writer(export_write)
        for i in export_list:
            writing.writerow(i)


export(scrape())
