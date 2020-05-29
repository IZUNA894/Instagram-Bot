# script for insta automation
#login to page,go to account ,
#find the followers
#find the following
#then match the followers and following ,
#and removes the extra following accounts that does not follows you back
#helpful in large page maintainence
#with following and followers in K's
#tried and tested on my page ....
#this code is writeen on jupyter notebook ,in form of blocks....
#every sparse line mark the beginning of new block

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path='C:\\Users\\tony\Desktop\\slWb\chromedriver',)
driver.get('https://www.instagram.com/')
time.sleep(6)
username=driver.find_element_by_name("username")
username.clear()
username.send_keys('**************')
passw=driver.find_element_by_name("password")
passw.clear()
passw.send_keys('********')
s=driver.find_element_by_xpath('//button[contains(@class,"L3NKy   ")]')
s.click()
time.sleep(6)
s=driver.find_element_by_xpath('//button[contains(@class,"aOOlW   ")]')
s.click()

def goToOurPage():
    time.sleep(2)
    s=driver.find_elements_by_class_name('gmFkV')
    #print(s)
    s[0].click()

goToOurPage()

def follName():
    s=driver.find_elements_by_class_name('-nal3')
    s[1].click()
    time.sleep(2)
    p=driver.find_element_by_class_name('isgrP')
    p.click()
    followerList=[]
    j=0
    ka = driver.find_elements_by_class_name('_0imsa')
    length= len(ka)
    print('followers found are :' , length)
    while(j<10):
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        s=driver.find_elements_by_class_name('_0imsa')
        for i in s:
            followerList.append(i.text)
            j+=1
    #for i in range(length):
    #    print(followerList[i])
    driver.back()
    return followerList

followerList=follName()
print(followerList)

from selenium.webdriver.support.ui import WebDriverWait 
def following():
    followingRemoved = 0
    s=driver.find_elements_by_class_name('-nal3')
    s[2].click()
    time.sleep(3)
    # after click follower link, wait until dialog appear
    WebDriverWait(driver, 10).until(lambda d: d.find_element_by_css_selector('div[role="dialog"]'))
    #p=driver.find_element_by_class_name('isgrP')
    #p.click()
    time.sleep(3)
    #print(p)
    #i need a parent list ,so using this class
    s=driver.find_elements_by_xpath('//html//body//div[4]//div//div[2]//ul//div//li')
    #print(s)
    print('following found',len(s))
    #print(s)
    j=0
    followingList=[]
    name=''
    current_height=driver.execute_script('return document.body.scroll.Height;')
    
    print('printing followers list')
    for i in range(len(followerList)):
        print(followerList[i])
    print('******************************')
    while True:
        for i in s:
            name=i.find_element_by_class_name('_0imsa')
            followingList.append(name.text)
            if(name.text in followerList):
                print(name.text,'follows you')
            else:
                print(name.text,'not follows you')
                button = i.find_element_by_class_name('sqdOP')
                button.click()
                WebDriverWait(driver, 10).until(lambda d: d.find_element_by_css_selector('div[role="dialog"]'))
                dialog = driver.find_element_by_class_name('piCib')
                if(dialog):
                    print('dialog box found')
                    time.sleep(2)
                    button = driver.find_element_by_class_name('aOOlW,-Cab_')
                    button.click()
                    

                followingRemoved += 1 
                print('unfollowed')
            j+=1
            
            
            
        driver.execute_script('window.scrollTo(0,arguments[0]);',current_height)
        time.sleep(3)
        new_height=driver.execute_script('return document.body.scroll.Height;')
        if(new_height==current_height):
            break
        current_height=new_height
    driver.back()
    print('original following')
    print(followingList)
    print('no of following removed',followingRemoved)
    return followingRemoved
    
#print(followerList)
following()