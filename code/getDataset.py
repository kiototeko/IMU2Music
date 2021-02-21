from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time
import subprocess

#Pawerl Motyka: https://blog.j-labs.pl/2017/02/Selenium-Webdriver-browser-preferences-for-downloading-files

def __get_firefox_driver(download_dir):
        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference("browser.download.manager.showAlertOnComplete", False)
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")
        fp.set_preference("browser.download.folderList", 2)
        fp.set_preference("browser.download.dir", download_dir)
        return webdriver.Firefox(firefox_profile=fp)

def get_number_files(download_dir):
        process = subprocess.Popen('ls ' + download_dir + '*.zip | wc -l', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out,_ = process.communicate()
        
        return int(out)
        
process = subprocess.Popen('curl http://telmi.upf.edu/opendatabase/ | grep -oE "https://repovizz.upf.edu/repo/Vizz/[^\\"]+"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out,error = process.communicate()



urls = out.decode('ascii').split("\n")

file_urls = open("visited_urls.txt","a+")
file_urls.seek(0)
visited_urls = file_urls.read().split("\n")

download_dir = "/home/kiototeko/tareas/sensingiot/IMU2Music/data/"
browser = __get_firefox_driver(download_dir)

for url in urls:

        print(url)
        if(url in visited_urls):
                continue
        
        retry = 0

        while retry < 5:

                num_files = get_number_files(download_dir)

                try:

                        browser.get(url)


                        assert 'RepoVizz' in browser.title

                        streams = browser.execute_script("return fileProps")


                        for idx,i in enumerate(streams):
                                if("ROOT0_Mult0_Sens" in i["xmlID"]  or i["xmlID"] == "ROOT0_Mult0_Audi0_Pick0"):
                                        browser.execute_script("fileProps[arguments[0]].canvas = 0", idx)

                        #browser.execute_script("fileProps = arguments[0]", streams)

                        alerted = True
                        
                        
                        while(alerted):
                                print("wukap")
                                browser.execute_script("downloadCompleteDatapackActiveStreams()")

                                WebDriverWait(browser, 5).until(expected_conditions.alert_is_present())

                                browser.switch_to.alert.accept()
                                
                                try:
                                        alert = WebDriverWait(browser, 5).until(expected_conditions.alert_is_present())
                                        alert.accept()
                                        alerted = True
                                except:
                                        alerted = False
                        
                        print("hla")
                        while(True):
                                num_files2 = get_number_files(download_dir)
                                if(num_files2 > num_files):
                                        break
                        file_urls.write(url + '\n')
                        break
                except:
                        retry += 1
                        print("Retrying " + str(retry))
                        time.sleep(3)
                
        if(retry >= 5):
                print("WARNING: Could not access the page")
        
"""
assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()
"""
