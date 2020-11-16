import os
from selenium import webdriver
# import time


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(executable_path = "D:\Software\Selenium_Python\chromedriver_win32\chromedriver.exe", desired_capabilities=chromeOptions.to_capabilities())


#driver = webdriver.Firefox(executable_path = "D:\Software\Selenium_Python\geckodriver-v0.24.0-win64\geckodriver.exe")

#driver = webdriver.Ie(executable_path = "D:\Software\Selenium_Python\IEDriverServer_x64_3.14.0\IEDriverServer.exe")

#driver.get("https://www.google.com/")

driver.get("https://www.google.com/")

# time.sleep(5)
# print(driver.title)
# print(driver.current_url)
# #driver.find_element_by_xpath()
#
# driver.close()