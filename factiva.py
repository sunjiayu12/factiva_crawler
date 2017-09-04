from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import csv
import random
import winsound

username = ["nju1", "nju2", "nju3"]
passwd = "njufactiva"

def isElementExist(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False

def url1(driver):
    url = "http://library.ust.hk/cgi/db/factiva.pl"
    driver.get(url)
    driver.find_element_by_xpath("/html/body/div[2]/h2/a").click()
    driver.find_element_by_xpath("/html/body/div/form/table[2]/tbody/tr[1]/td[2]/input").send_keys("lxieac")
    driver.find_element_by_xpath("/html/body/div/form/table[2]/tbody/tr[3]/td[2]/input").send_keys("198968xy")
    driver.find_element_by_xpath("/html/body/div/form/table[2]/tbody/tr[4]/td[2]/input").click()
    sleep(30)

def login(driver, username, passwd):
    url2 = "https://global.factiva.com"
    driver.get(url2)
    # sleep(20)
    WebDriverWait(driver, 180, 0.5).until(lambda driver: driver.find_element_by_xpath("/html/body/section/div/div/div/div/div[1]/form/div/div[1]/div[1]/input"))
    sleep(2)
    driver.find_element_by_xpath("/html/body/section/div/div/div/div/div[1]/form/div/div[1]/div[1]/input").send_keys(username)
    driver.find_element_by_xpath("/html/body/section/div/div/div/div/div[1]/form/div/div[2]/div[1]/input").send_keys(passwd)
    sleep(1)
    driver.find_element_by_xpath("/html/body/section/div/div/div/div/div[1]/form/div/div[7]/div/button").click()
    # sleep(30)


articleFound = True

def process(driver, data, rand):
    global articleFound
    # input conm
    driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]").send_keys(data[1])

    # input date
    if(rand == 0):
        driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[3]/div[1]/table/tbody/tr/td[1]/select/option[10]").click()
        driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[3]/div[1]/table/tbody/tr/td[2]/div/input[1]").send_keys(str(int(data[0]) - 1)+"0101")
        driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[3]/div[1]/table/tbody/tr/td[2]/div/input[7]").send_keys(str(int(data[0]) + 1)+"1231")
    if(rand == 1 or rand == 2):
        driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[3]/div[1]/table/tbody/tr/td[1]/select/option[10]").click()
        driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[3]/div[1]/table/tbody/tr/td[2]/div/input[1]").send_keys("01")
        driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[3]/div[1]/table/tbody/tr/td[2]/div/input[2]").send_keys("01")
        driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[3]/div[1]/table/tbody/tr/td[2]/div/input[3]").send_keys(str(int(data[0]) - 1))
        driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[3]/div[1]/table/tbody/tr/td[2]/div/input[9]").send_keys("31")
        driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[3]/div[1]/table/tbody/tr/td[2]/div/input[10]").send_keys("12")
        driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[3]/div[1]/table/tbody/tr/td[2]/div/input[11]").send_keys(str(int(data[0]) + 1))

    # input sources
    driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[3]/td[1]/a").click()
    if(rand == 0):
        WebDriverWait(driver, 180, 0.5).until(lambda driver: driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[4]/td[2]/div[3]/ul/li[2]/a[1]"))
        sleep(2)
        driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[4]/td[2]/div[3]/ul/li[2]/a[1]").click()
    if(rand == 1 or rand == 2):
        WebDriverWait(driver, 180, 0.5).until(lambda driver: driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[4]/td[2]/div[3]/ul/li[1]/a[1]"))
        sleep(2)
        driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[4]/td[2]/div[3]/ul/li[1]/a[1]").click()

    # input more options
    WebDriverWait(driver, 180, 0.5).until(lambda driver: driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[21]/td[1]/a"))
    sleep(2)
    driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[21]/td[1]/a").click()
    driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[22]/td[2]/div/div/table/tbody/tr[1]/td[2]/select/option[3]").click()

    # search
    driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/div[2]/ul/li[3]/input").click()

    WebDriverWait(driver, 180, 0.5).until(lambda driver: driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div[6]/div[1]/table[2]/tbody/tr/td/div/div[2]/span[2]/div[1]/a"))
    sleep(2)

    # set display option
    driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div[6]/div[1]/table[2]/tbody/tr/td/div/div[2]/span[2]/div[1]/a").click()
    driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div[6]/div[1]/table[2]/tbody/tr/td/div/div[2]/span[2]/div[2]/div[1]/ul/li[3]/a").click()

    # if no article found
    if(not isElementExist(driver, "/html/body/form[2]/div[2]/div[2]/div[6]/div[2]/div[3]/div/div[1]/div/div[1]/table/tbody/tr/td/span[1]/input")):
        articleFound = False
        # winsound.Beep(1000, 500)
    else:
        articleFound = True
        # select all articles
        driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div[6]/div[2]/div[3]/div/div[1]/div/div[1]/table/tbody/tr/td/span[1]/input").click()

        # download rtf
        driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div[6]/div[1]/table[2]/tbody/tr/td/div/div[1]/span[3]/ul/li[6]/a").click()
        # sleep(2)
        driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div[6]/div[1]/table[2]/tbody/tr/td/div/div[1]/span[3]/ul/li[6]/ul/li[2]/a").click()
        sleep(16)
        # winsound.Beep(1000, 500)

if __name__ == '__main__':
    reader = csv.reader(open('exercise.csv', 'r'))
    i = 1

    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.dir", "E:\\Factiva\\data_downloads")
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/rtf")
    driver = webdriver.Firefox(firefox_profile=profile)

    rand = random.randint(0, 0)
    print("Using ID: " + username[rand])
    login(driver, username[rand], passwd)

    WebDriverWait(driver, 180, 0.5).until(lambda driver: driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/input[2]"))
    sleep(2)

    for data in reader:
        writer = csv.writer(open('res2.csv', 'a', newline=''), dialect='excel')
        print("No." + str(i) + ": started downloading")
        driver.get("https://global.factiva.com/sb/default.aspx?NAPC=S")
        WebDriverWait(driver, 180, 0.5).until(lambda driver: driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[2]/div/div[2]/ul/li[3]/input"))
        sleep(2)
        process(driver, data, rand)
        if(articleFound == True):
            writer.writerow(data)
        else:
            data.append("article not found")
            writer.writerow(data)
        print("No." + str(i) + ": finished downloading")
        print("-----------------------------------------------------------")
        i = i + 1