from tkinter.ttk import Separator
import requests
from bs4 import BeautifulSoup
import csv

def get_fnumbers():
    fnum_list = []
    url = "http://federbridge.it/SocSp/ChkFS.asp?FS=F"
    
    response = requests.get(url)
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    fnumbers = soup.select('span.COLviolaChiaro')   
    for fnum in fnumbers:
        if fnum.text[0] == "F":
            fnum_list.append(fnum.text)
    return fnum_list

def detail_page(fnumber):
    response = requests.get(f"https://federbridge.it/regioni/dettASS.asp?codice={fnumber}")
    soup = BeautifulSoup(response.text, 'html.parser')
    name = soup.select_one("td.FNTbase12").text
    email = soup.select_one("td.ALLbaseR a[href^='mailto']").text
    return name, email

def save_to_csv(output):
    with open("results.csv", "w") as f:
        csv_writer = csv.writer(f, delimiter=",")
        for item in output:
            csv_writer.writerow(item)

def main():
    results = []
    numbers = get_fnumbers()
    for num in numbers[:10]:
        results.append(detail_page(num))
        print(num)
    print(results)
    save_to_csv(results)

if __name__ == "__main__":
    main()