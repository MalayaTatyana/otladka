import csv
import time
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
lines = []
lines2 = []

def init():
    with open("test10.csv") as sites:
        reader = csv.DictReader(sites, delimiter = ',')
        for line in reader:
            lines.append(line["URL"])
            lines2.append(line["URL"])

def sort_and_open():
    lines.sort(key=len)
    lines2.sort()
    for url in lines:
        print("Открываю "+url)
        open_next_url(url)
    driver.close()

def open_next_url(url):
    driver.get(url)
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[-1])

def close_next_url():
    for l in lines:
        if l.find(lines2[0])!=-1:
            driver.switch_to.window(driver.window_handles[lines.index(l)])
            time.sleep(3)
            driver.close()
            lines2.remove(lines2[0])
            lines.remove(l)
            return

if __name__ == "__main__":
    init()
    sort_and_open()
    input("Нажмите Enter для продолжения...")
    while len(lines)>0:
        time.sleep(2)
        print("Через 3 секунды закрываю текущую вкладку (" + lines2[0]+")")
        close_next_url()
        
