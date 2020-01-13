from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
url = "https://sprungmarker.de/"
cloud = []
posts = []
driver.get(url)


def tag_cloud_processing(): #обработка облака тэгов
    for link in driver.find_elements_by_class_name("tag-cloud-link"):
        cloud.append(link.text.lower())
    print("\nОблако тегов содержит следующие слова:")
    for index, c in enumerate(cloud):
        if index%3==0: 
            print ("")
        print ("%-5i%-20s"%(index,c), end=" ")
    print ("") 

def check_tags_in_posts(posts):
    flag=True
    for p in posts:
        print("\n")
        print(p+"\n")
        driver.get(p)
        tags=[]
        for tag in driver.find_elements_by_xpath('//span[@class="tags-links"]/a'):
            tags.append(tag.text.lower())
        for  tag in tags:                  
            if tag in cloud:                   
                print("   %-20s"%tag+str(cloud.index(tag)))
            else:
                print("   %-20s"%tag+"ОТСУТСТВУЕТ")
                flag=False
    return flag
if __name__ == "__main__":
    tag_cloud_processing()
    for link in driver.find_elements_by_xpath('//h3[@class="entry-title"]/a'):
        posts.append(link.get_attribute("href"))
    if check_tags_in_posts(posts):
        print("\n\n     Все теги постов на главной странице присутствуют в облаке тегов. ")
    else:
        print("\n\n     В облаке тегов отсутствуют некоторые теги из постов, \n     расположенных на главной странице.")


    
    driver.get(url)
    input("\n\nНажмите Enter для закрытия браузера...")
    driver.close()
