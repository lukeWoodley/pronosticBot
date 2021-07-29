from selenium import webdriver
import time
import pyautogui
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os

PATH  = 'C:\Program Files (x86)\chromedriver.exe'

xPath = '//*[@id="app"]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div[1]/div/div[3]/span/span[1]' # button no 3
xPath2 = '//*[@id="app"]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div[1]/div/div[4]/span/span[1]' #button no 4
xPath3 = '//*[@id="app"]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div[1]/div/div[5]/span/span[1]' #button no 5
xPathArray = [xPath, xPath2, xPath3]

expandButtonXPath = '//*[@id="app"]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[1]/div[2]/div[3]/div/div[1]'
titleScoreExactXPath = '//*[@id="app"]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[1]/div[1]/div[1]'

startTimeinH = 23
finishTimeinH = 7


# arrayMatchAndLink = [
#                     ['Central Cordoba Sde vs CA Talleres',              'https://www.winamax.fr/paris-sportifs/match/27959192', xPath2],
#                     ['Arsenal Sarandi vs Argentinos Juniors',          'https://www.winamax.fr/paris-sportifs/match/27959188', xPath2],
#                     ['Gimnasia La Plata vs Rosario Central',              'https://www.winamax.fr/paris-sportifs/match/27959194', xPath2],
#                     ['Newells Old Boys vs Estudiantes', 'https://www.winamax.fr/paris-sportifs/match/27959204', xPath2],
#
#                     ['Deportes Antofagasta vs Universidad Catolica',             'https://www.winamax.fr/paris-sportifs/match/27207572', xPath2],
#                     ['Universidad De Chile vs Nublense',                     'https://www.winamax.fr/paris-sportifs/match/27207566', xPath2]
#
# ]


arrayMatchAndLink = [
                    ['Central Cordoba Sde vs CA Talleres',              'https://www.winamax.fr/paris-sportifs/match/27959192'],
                    ['Arsenal Sarandi vs Argentinos Juniors',          'https://www.winamax.fr/paris-sportifs/match/27959188'],
                    ['Gimnasia La Plata vs Rosario Central',              'https://www.winamax.fr/paris-sportifs/match/27959194'],
                    ['Newells Old Boys vs Estudiantes', 'https://www.winamax.fr/paris-sportifs/match/27959204'],

                    ['Deportes Antofagasta vs Universidad Catolica',             'https://www.winamax.fr/paris-sportifs/match/27207572'],
                    ['Universidad De Chile vs Nublense',                     'https://www.winamax.fr/paris-sportifs/match/27207566']


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
        time.sleep(3)
        indexTab = 0
        for row in arrayMatchAndLink:
            driver.switch_to.window(driver.window_handles[indexTab])
            driver.refresh()
            time.sleep(5)
            driver = goToScoreExact(driver, row)
            time.sleep(0.7)
            takeScreenshot(row[0])
            indexTab = indexTab + 1
        time.sleep(getCurrentSeconds())

    # buttonScoreExact = driver.find_element_by_xpath(row[2])
    # buttonScoreExact.click()


def goToScoreExact(driver, row):
    clickButton(driver, row)
    time.sleep(0.3)
    expandButton = driver.find_element_by_xpath(expandButtonXPath)
    expandButton.click()
    driver.find_element_by_xpath(titleScoreExactXPath).location_once_scrolled_into_view
    time.sleep(0.3)

    return driver

def clickButton(driver, row):
    compteur = 0
    for xpath in xPathArray:
        try:
            buttonScoreExact = driver.find_element_by_xpath(xpath)
            if buttonScoreExact.text == "Score exact":
                print("test")
                buttonScoreExact.click()
                buttonScoreExact.location_once_scrolled_into_view
                return
        except Exception:
            compteur = compteur + 1



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
    if current_time != finishTimeinH:
        return True
    else:
        os.system("shutdown /s /t 1")
        quit()
        return False

def shouldStart():
    now = datetime.now()
    current_time = int(now.strftime("%H"))
    if current_time != startTimeinH:
        return False
    return True

if __name__ == '__main__':
    while True:
        if shouldStart():
            launchSelenium()
        print("not time yet...")
        time.sleep(60)


