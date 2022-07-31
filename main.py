from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import urllib.request
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

    ctypes.windll.kernel32.SetConsoleTitleW(f"Facebook album scraper | by fema3832")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    albumlink = input("album link: ")
    driver.get(albumlink)
    driver.maximize_window()
    time.sleep(2)

    #* COOKIES =============================
    okay = driver.find_element(By.XPATH, r'//*[@id="facebook"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div')
    okay.click()

    #* DOWNLOADING =============================
    while True:
        image = ''
        imgsrc = ''
        nextpage = ''
        currentimgname = ''

        #* IMG SOURCE =============================
        time.sleep(2)
        image = driver.find_element(By.XPATH, r'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/img')
        imgsrc = image.get_attribute('src')
        currentimgname = imgsrc[53:60]

        if gotname == False:
            firstname = currentimgname
            gotname = True

        #* NEXT PAGE =============================
        time.sleep(2)
        if currentimgname != oldimgname or currentimgname != firstname:
            dl_jpg(imgsrc, foldername, currentimgname)
            nextpage = driver.find_element(By.XPATH, r'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div/div[1]/div[3]/div')
            driver.execute_script("arguments[0].click();", nextpage)
            oldimgname = currentimgname
        else:
            print('Finished')
            driver.quit()

dl_img('images')