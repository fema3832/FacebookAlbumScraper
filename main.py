from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import urllib.request
from sys import exit
import ctypes
import time
import os

# * DOWNLOAD IMAGE FUNCTION =============================
def dl_jpg(url, file_path, file_name):
    if not os.path.exists(os.getcwd() + f'/{file_path}'):
        os.makedirs(os.getcwd() + f'/{file_path}')
    fullpath = f'{file_path}/' + file_name + '.jpg'
    urllib.request.urlretrieve(url, fullpath)
    print(f'{file_name} downloaded to {file_path}')

# * DOWNLOAD IMAGE =============================
def dl_img(foldername):
    firstname = ''
    gotname = False
    oldimgname = ''
    tempnum = 0

    ctypes.windll.kernel32.SetConsoleTitleW(f"Facebook album scraper | by fema3832")
    albumlink = input("album link: ")
    option = webdriver.ChromeOptions()
    option.add_argument("disable-logging")
    option.add_argument("log-level=3")
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=option, service=Service(ChromeDriverManager().install()))
    driver.get(albumlink)
    time.sleep(2)

    #* COOKIES =============================
    okay = driver.find_element(By.XPATH, r'/html/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]')
    okay.click()

    #* DOWNLOADING =============================
    while True:
        image = ''
        imgsrc = ''
        nextpage = ''
        currentimgname = ''

        #* IMG SOURCE =============================
        time.sleep(1)
        image = driver.find_element(By.XPATH, r'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/img')
        time.sleep(1)
        imgsrc = image.get_attribute('src')
        currentimgname = imgsrc[53:60]

        if gotname == False:
            firstname = currentimgname
            gotname = True

        #* NEXT PAGE =============================
        time.sleep(1)
        if currentimgname != oldimgname:
            if currentimgname != firstname or tempnum == 0:
                tempnum = tempnum + 1
                dl_jpg(imgsrc, foldername, currentimgname)
                time.sleep(1)
                nextpage = driver.find_element(By.XPATH, r'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div/div[1]/div[3]/div')
                driver.execute_script("arguments[0].click();", nextpage)
                oldimgname = currentimgname
            else:
                print('Finished')
                time.sleep(5)
                driver.quit()
                exit(0)
                
        else:
            print('Finished')
            time.sleep(5)
            driver.quit()
            exit(0)

dl_img('images')
