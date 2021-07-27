from selenium import webdriver
import time
import pyautogui
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os

PATH  = 'C:\Program Files (x86)\chromedriver.exe'
xPath = '//*[@id="app"]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div[1]/div/div[3]/span/span[1]'
arrayMatchAndLink = [
                    ['Sao Paulo vs Palmeiras',      'https://www.winamax.fr/paris-sportifs/match/27471696'],
                    ['Internacional vs Cuiaba MT',  'https://www.winamax.fr/paris-sportifs/match/27471694'],
                    ['Bragantino SP vs Grêmio',     'https://www.winamax.fr/paris-sportifs/match/27471684'],
                    ['Corinthians vs Flamengo',     'https://www.winamax.fr/paris-sportifs/match/27471690']

]



def launchSelenium():
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()
    time.sleep(2)
    openAllTabs(driver)


def openAllTabs(driver):
    while True:
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

        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)
        indexTab = 0
        for row in arrayMatchAndLink:
            driver.switch_to.window(driver.window_handles[indexTab])
            driver.refresh()
            time.sleep(3)
            driver = goToScoreExact(driver)
            takeScreenshot(row[0])
            indexTab = indexTab + 1
        time.sleep(getCurrentSeconds())


def goToScoreExact(driver):
    buttonScoreExact = driver.find_element_by_xpath(xPath)
    buttonScoreExact.click()
    buttonScoreExact.location_once_scrolled_into_view
    return driver


def getCurrentSeconds():
   now = datetime.now()
   current_time = int(now.strftime("%S"))
   return 60-current_time


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


if __name__ == '__main__':
    launchSelenium()



