from selenium import webdriver
import time
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
driver=webdriver.Chrome(executable_path="D:\Software\Selenium_Python\chromedriver_win32\chromedriver.exe", desired_capabilities = chromeOptions.to_capabilities())
driver.implicitly_wait(5)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath("//button[contains(text(),'Click Me')]").click()
time.sleep(2)
#driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()
time.sleep(2)
driver.quit()