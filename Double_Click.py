import time
from selenium import webdriver
from selenium.webdriver import ActionChains
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
driver=webdriver.Chrome(executable_path="D:\Software\Selenium_Python\chromedriver_win32\chromedriver.exe", desired_capabilities = chromeOptions.to_capabilities())
driver.implicitly_wait(5)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)
element = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
actions = ActionChains(driver)
time.sleep(2)
actions.double_click(element).perform()
time.sleep(2)
driver.quit()
