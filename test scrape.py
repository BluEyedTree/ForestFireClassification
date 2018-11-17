from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib
import argparse
from urllib.request import Request, urlopen

searchterm = 'Colorado Forest Fall' # will also be the name of the folder
url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
# NEED TO DOWNLOAD CHROMEDRIVER, insert path to chromedriver inside parentheses in following line
browser = webdriver.Chrome("/Users/thomasbekman/Downloads/chromedriver")
browser.get(url)
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
counter = 0
succounter = 0


def downloadImage(fileName, url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    webpage = urlopen(req).read()
    file = open(fileName, "wb")
    file.write(webpage)

if not os.path.exists(searchterm):
    os.mkdir(searchterm)

for _ in range(2000):
    browser.execute_script("window.scrollBy(0,10000)")


for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
    counter = counter + 1
    print ("Total Count:", counter)
    print ("Succsessful Count:", succounter)
    print ("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])
    URL = json.loads(x.get_attribute('innerHTML'))["ou"]

    try:
        img = json.loads(x.get_attribute('innerHTML'))["ou"]
        imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
        downloadImage("G"+str(counter)+".jpg", URL)
    except:
        print("I failed")
browser.close()