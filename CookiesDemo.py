import time
from selenium import webdriver
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
driver=webdriver.Chrome(executable_path="D:\Software\Selenium_Python\chromedriver_win32\chromedriver.exe", desired_capabilities = chromeOptions.to_capabilities())
driver.implicitly_wait(5)
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(2)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
time.sleep(2)
cookie = {'name':'Amit','value':'1234567890'}
driver.add_cookie(cookie)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
time.sleep(2)
driver.delete_cookie('Amit')
time.sleep(2)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
time.sleep(2)
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
time.sleep(2)
driver.quit()
