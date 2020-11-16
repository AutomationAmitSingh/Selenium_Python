import time
from selenium import webdriver
from selenium.webdriver.common.by import By
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
driver=webdriver.Chrome(executable_path="D:\Software\Selenium_Python\chromedriver_win32\chromedriver.exe", desired_capabilities = chromeOptions.to_capabilities())
driver.implicitly_wait(5)
driver.get("http://www.newtours.demoaut.com/")
driver.maximize_window()
time.sleep(2)
links = driver.find_elements(By.TAG_NAME,"a")
print(" Number of links present : ",len(links))
for link in links:
    print(link.text)

time.sleep(2)
driver.find_element(By.LINK_TEXT,"REGISTER").click()
time.sleep(2)
driver.quit()