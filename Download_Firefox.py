import time
from selenium import webdriver
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf")
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir","D:\Bin")
fp.set_preference("browser.download.folderList",2)
fp.set_preference("pdfjs.disabled",True)
driver = webdriver.Firefox(executable_path = "D:\Software\Selenium_Python\geckodriver-v0.24.0-win64\geckodriver.exe",firefox_profile=fp)
driver.implicitly_wait(5)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_id("textbox").send_keys("testng download text file")
time.sleep(2)
driver.find_element_by_id("createTxt").click()
time.sleep(2)
driver.find_element_by_id("link-to-download").click()
time.sleep(2)
driver.find_element_by_id("pdfbox").send_keys("testng download pdf file")
time.sleep(2)
driver.find_element_by_id("createPdf").click()
time.sleep(2)
driver.find_element_by_id("pdf-link-to-download").click()
time.sleep(2)
driver.quit()