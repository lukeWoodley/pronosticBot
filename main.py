from selenium import webdriver
import time
import pyautogui
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

PATH  = 'C:\Program Files (x86)\chromedriver.exe'
xPath = '//*[@id="app"]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div[1]/div/div[5]/span/span[1]'
arrayMatchAndLink = [
                    ['Atlético Mineiro vs Bahia: Bresil Serie A','https://www.winamax.fr/paris-sportifs/match/27471658'],
                    ['Huachipato vs Deportes La Serena: Chili premiere division','https://www.winamax.fr/paris-sportifs/match/27207554'],
                    ['Changchun Yatai vs Dalian Professional FC: Chine super League','https://www.winamax.fr/paris-sportifs/match/28141760'],
                    ['Bucaramanga vs Santa Fe: Colombie Primera A, Clausura','https://www.winamax.fr/paris-sportifs/match/28224720']
]


def launchSelenium():
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()
    time.sleep(10)
    #openAllTabs(driver)

   # print("come here!")
   #time.sleep(10)
   #driver.navigate.refresh()

def openAllTabs(driver):
    i = 0
    firstWindow = driver.window_handles[0]
    firstWindow = "tab1"

    for row in arrayMatchAndLink:
        if i == 0:
            driver.get(row[1])
        else:
            nameOfTab = tab + str(i)
            command = "window.open('about:blank','" + nameOfTab + "');"
            driver.execute_script(command)
            driver.switch_to.window(nameOfTab)
            driver.get(row[1])
            time.sleep(3)
            driver = goToScoreExact(driver)
            takeScreenshot(row[0])

    driver.get('https://www.winamax.fr/paris-sportifs/match/27471658')
    driver.maximize_window()
    driver.execute_script("window.open('about:blank','secondtab');")
    driver.switch_to.window("secondtab")
    driver.get('https://www.winamax.fr/paris-sportifs/match/27471658')


def goToScoreExact(driver):
    buttonScoreExact = driver.find_element_by_xpath(xPath)
    buttonScoreExact.click()
    buttonScoreExact.location_once_scrolled_into_view
    return driver




   # driver = webdriver.Chrome(PATH)
   # driver.get('https://www.winamax.fr/paris-sportifs/match/28200766')#https://www.winamax.fr/paris-sportifs/match/28200766  #https://www.winamax.fr/paris-sportifs/match/27471666
   # driver.maximize_window()
   # while True:
   #    driver.get('https://www.winamax.fr/paris-sportifs/match/27471666')
   #    driver.maximize_window()
   #    time.sleep(getCurrentSeconds())
   #    buttonScoreExact = driver.fignd_element_by_xpath(
   #       '//*[@id="app"]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div[1]/div/div[5]/span/span[1]')
   #    buttonScoreExact.click()
   #    buttonScoreExact.location_once_scrolled_into_view
   #    time.sleep(2)
   #    takeScreenshot(driver)




def getCurrentSeconds():
   now = datetime.now()
   current_time = int(now.strftime("%S"))
   return 60-current_time





def takeScreenshot(folderName):
   now = datetime.now()
   current_time = now.strftime("%d_%m_%Y %H_%M_%S")
   myscreen = pyautogui.screenshot()
   pathScreenShot = folderName + "/" + current_time+".png"
   print(pathScreenShot)
   myscreen.save(pathScreenShot)


if __name__ == '__main__':
    launchSelenium()



