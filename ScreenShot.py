import time
from selenium import webdriver
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
driver=webdriver.Chrome(executable_path="D:\Software\Selenium_Python\chromedriver_win32\chromedriver.exe", desired_capabilities = chromeOptions.to_capabilities())
driver.implicitly_wait(5)
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
#driver.get_screenshot_as_file("D:\ScreenShot\ScreenShot1.pngddddddddddddd")
driver.save_screenshot("D:\ScreenShot\ScreenShot1.jpg")
time.sleep(2)
driver.quit()