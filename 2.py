from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
list = ['esc','3','2', 'enter']
operation=[('minus','-'), ('mult', '/'), ('plus','*')]
driver = webdriver.Chrome('chromedriver.exe')
url = "https://calc.by/math-calculators/scientific-calculator.html#!"
driver.get(url)
def check(i):
        elem=driver.find_element_by_id("btn_"+i)
        elem.click()
        res_text = driver.find_element_by_id("calc_display_input").get_attribute("value")
        assert res_text==i, "ne"+i
        print(i)
def verification(o):
        list.insert(2,o[0])
        for l in list:
                driver.find_element_by_id("btn_"+l).click()
        if driver.find_element_by_id("calc_display_input").get_attribute("value")==str(eval('3 '+o[1]+' 2')):
                print('Проверка оператора '+ o[1])
        else:
                print ('error c '+ o[1])
        print('3 '+ o[1]+' 2 = ',str(eval('3 '+o[1]+' 2')))
        list.pop(2)
if __name__ == "__main__":
        for i in range (10):
                driver.find_element_by_id("btn_esc").click()
                check(str(i))
        for o in operation:
                verification(o)
        input("Нажмите Enter чтобы закрыть браузер...")
        driver.close()
