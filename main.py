from selenium import webdriver
import time
import pyautogui
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os

PATH  = 'C:\Program Files (x86)\chromedriver.exe'

xPath = '//*[@id="app"]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div[1]/div/div[3]/span/span[1]'
xPath2 = '//*[@id="app"]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div[1]/div/div[4]/span/span[1]'
xPath3 = '//*[@id="app"]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div[1]/div/div[5]/span/span[1]'



arrayMatchAndLink = [
                    ['Audax Italiano vs Everton',                    'https://www.winamax.fr/paris-sportifs/match/27207560', xPath2],
                    ['Vikingur Gota vs Runavik',                     'https://www.winamax.fr/paris-sportifs/match/25853620', xPath2],
                    ['07 Vestur Sorvagur vs Streymur',               'https://www.winamax.fr/paris-sportifs/match/25853616', xPath],
                    ['La Equidad vs Pasto',                          'https://www.winamax.fr/paris-sportifs/match/28224728', xPath3],
                    ['Huracan vs Colon De Santa Fe',                 'https://www.winamax.fr/paris-sportifs/match/27959198', xPath2],
                    ['Aldosivi vs Racing Club',                      'https://www.winamax.fr/paris-sportifs/match/27959186', xPath2]

]





def launchSelenium():
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()
    time.sleep(2)
    openAllTabs(driver)


def openAllTabs(driver):
    firstIteration = True
    i = 2

    for row in arrayMatchAndLink:
        if firstIteration:
            driver.get(row[1])
            firstIteration = False
        else:
            nameOfTab = "tab" + str(i)
            command = "window.open('about:blank','" + nameOfTab + "');"
            driver.execute_script(command)
            driver.switch_to.window(nameOfTab)
            driver.get(row[1])
        i = i + 1

    while notFinished():
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)
        indexTab = 0
        for row in arrayMatchAndLink:
            driver.switch_to.window(driver.window_handles[indexTab])
            driver.refresh()
            time.sleep(3)
            driver = goToScoreExact(driver, row)
            time.sleep(0.2)
            takeScreenshot(row[0])
            indexTab = indexTab + 1
        time.sleep(getCurrentSeconds())




def goToScoreExact(driver, row):
    buttonScoreExact = driver.find_element_by_xpath(row[2])
    buttonScoreExact.click()
    buttonScoreExact.location_once_scrolled_into_view
    return driver


def getCurrentSeconds():
   now = datetime.now()
   current_time = int(now.strftime("%S"))
   return 120-current_time


def takeScreenshot(folderName):
   now = datetime.now()
   current_time = now.strftime("%d_%m_%Y %H_%M_%S")
   myscreen = pyautogui.screenshot()
   pathScreenShot =  folderName + "/" + current_time+".png"
   print(pathScreenShot)
   os.chdir("matches_pictures/")
   createDirectory(folderName)
   myscreen.save(pathScreenShot)
   os.chdir("..")

def createDirectory(folderName):
    try:
        os.mkdir(folderName)
    except OSError as error:
        pass

def notFinished():
    now = datetime.now()
    current_time = int(now.strftime("%H"))
    if current_time != 7:
        return True
    else:
        quit()
        return False

def shouldStart():
    now = datetime.now()
    current_time = int(now.strftime("%H"))
    if current_time != 1:
        return False
    return True

if __name__ == '__main__':
    while True:
        time.sleep(60)
        if shouldStart():
            launchSelenium()




