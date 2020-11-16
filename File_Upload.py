import time
from selenium import webdriver
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
driver=webdriver.Chrome(executable_path="D:\\Software\Selenium_Python\\chromedriver_win32\\chromedriver.exe", desired_capabilities = chromeOptions.to_capabilities())
driver.implicitly_wait(5)
driver.get("https://testautomationpractice.blogspot.com/")
driver.switch_to.frame(0)
driver.maximize_window()
driver.find_element_by_id("RESULT_FileUpload-11").send_keys("C:\\Users\z003tnxs\\Downloads\\code.txt")
time.sleep(4)
#driver.quit()
