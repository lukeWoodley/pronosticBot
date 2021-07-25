from selenium import webdriver
import time
import pyautogui
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

PATH  = 'C:\Program Files (x86)\chromedriver.exe'

def launchSelenium():
   driver = webdriver.Chrome(PATH)
   driver.get('https://www.winamax.fr/paris-sportifs/match/27471658')#https://www.winamax.fr/paris-sportifs/match/28200766  #https://www.winamax.fr/paris-sportifs/match/27471666
   driver.maximize_window()
   while True:
      driver.get('https://www.winamax.fr/paris-sportifs/match/27471658')
      driver.maximize_window()
      time.sleep(getCurrentSeconds())
      buttonScoreExact = driver.find_element_by_xpath(
         '//*[@id="app"]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div[1]/div/div[5]/span/span[1]')
      buttonScoreExact.click()
      buttonScoreExact.location_once_scrolled_into_view
      time.sleep(2)
      takeScreenshot(driver)




def getCurrentSeconds():
   now = datetime.now()
   current_time = int(now.strftime("%S"))
   return 60-current_time





def takeScreenshot(driver):
   now = datetime.now()
   current_time = now.strftime("%d_%m_%Y %H_%M_%S")
   myscreen = pyautogui.screenshot()
   pathScreenShot = "my_pictures/" + current_time+".png"
   print(pathScreenShot)
   myscreen.save(pathScreenShot)


if __name__ == '__main__':
    launchSelenium()



