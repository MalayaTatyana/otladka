from selenium import webdriver
from selenium.webdriver.common.keys import Keys
"""
Открыть поисковый сайт 
Последовательно набирать поисковые словосочетания: 
Недвижимость в Португалии, Недвижимость в Финляндии, Недвижимость в Италии. 
После набора каждого из указанных словосочетаний запускать поиск. 
Затем последовательно набрать поисковые словосочетания Test, Testcase, Testplan, после каждого набора запустить поиск. 
По результатам каждого поиска определить количество появлений слова Недвижимость 
                       на первой странице каждого из открытых по результатам поиска сайтов.
"""

driver = webdriver.Chrome()
requests = ["Недвижимость в Португалии", "Недвижимость в Финляндии", "Недвижимость в Италии", 
"Test", "Testcase", "Testplan"]
text = []

def search(text):
    search_line = driver.find_element_by_class_name("gLFyf.gsfi")
    search_line.clear()
    search_line.send_keys(text+Keys.ENTER)

def count_r():
    count_words = 0
    text=[]
    for t in driver.find_elements_by_xpath('//span[@class="st"]'):
        text.append(t.text.lower())
    for t in text:
        count_words+= t.count("Недвижимость".lower())
    return(str(count_words))

if __name__ == "__main__":
    driver.get("https://www.google.com")
    print('Количество появлений слова "Недвижимость" по следующим запросам:')
    for r in requests:
        search(r)
        print(r+": "+ count_r())
    driver.close()
