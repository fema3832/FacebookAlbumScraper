from selenium import webdriver
import urllib.request
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
    path = r'C:\Users\user\Documents\chromedriver.exe'
    oldimgname = ''

    driver = webdriver.Chrome(path)
    driver.get('album name')
    driver.maximize_window()
    time.sleep(2)

    #* COOKIES =============================
    okay = driver.find_element_by_xpath(r'//*[@id="facebook"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div')
    okay.click()

    #* DOWNLOADING =============================
    while True:
        image = ''
        imgsrc = ''
        nextpage = ''
        currentimgname = ''

        #* IMG SOURCE =============================
        time.sleep(2)
        image = driver.find_element_by_xpath(r'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/img')
        imgsrc = image.get_attribute('src')
        currentimgname = imgsrc[53:60]

        #* NEXT PAGE =============================
        time.sleep(2)
        if currentimgname != oldimgname:
            dl_jpg(imgsrc, foldername, currentimgname)
            nextpage = driver.find_element_by_xpath(r'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div/div[1]/div[3]/div')
            driver.execute_script("arguments[0].click();", nextpage)
            oldimgname = currentimgname
        else:
            print('Finished')
            driver.quit()

dl_img('images')