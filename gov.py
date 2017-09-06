from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import csv
import win32api
import win32con
import os, sys
import shutil

title = "TITLE"
author = "AUTHOR"
fileName = "IAMASTRING"
matched = True

def isElementExist(driver, element):
    try:
        driver.find_element_by_xpath(element)
        return True
    except:
        return False

def process(driver, city):
    global title, author, fileName, matched
    driver.get("http://navi.cnki.net/KNavi/NPaper.html")
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[2]/input[1]").send_keys(city+"日报")
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[2]/input[2]").click()
    sleep(5)
    new_url = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div/div[2]/ul/li/a").get_attribute("href")
    driver.get(new_url)
    sleep(5)
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/ul[2]/div[2]/input[4]").send_keys("政府工作报告")
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/ul[2]/div[2]/a").click()
    sleep(5)
    for i in range(1, 21):
        if (driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/table/tbody/tr[" + str(i) + "]/td[2]/a/font").text == "政府工作报告"):
            matched = True
            title = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/table/tbody/tr[" + str(i) + "]/td[2]/a").text
            date = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/table/tbody/tr[" + str(i) + "]/td[6]").text
            fileName = city + "_" + title + "_" + date
            test_string = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/table/tbody/tr[" + str(i) + "]/td[2]/a").get_attribute("href")
            new_url = "http://kns.cnki.net/kcms/detail/detail.aspx?" + test_string[-60:]
            driver.get(new_url)
            author = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div[1]/span/a").text
            driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[1]/div[2]/a[2]").click()
            sleep(10)
            win32api.SetCursorPos((723, 595))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 723, 595, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 723, 595, 0, 0)
            sleep(5)
            shutil.move("C:\\Users\\sunjiayu\\Desktop\\gov\\"+title+"_"+author+".pdf", "C:\\Users\\sunjiayu\\Desktop\\gov\\data\\" + fileName + ".pdf")
            driver.quit()
        else:
            continue
            driver.quit()

if __name__ == '__main__':
    cities = csv.reader(open("source.csv", "r", encoding="utf-8"))
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.dir", "C:\\Users\\sunjiayu\\Desktop\\gov")
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    driver = webdriver.Firefox(firefox_profile=profile)
    for city in cities:
        process(driver, city[0])