import time
from selenium import webdriver
from selenium.webdriver import ActionChains
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
driver=webdriver.Chrome(executable_path="D:\Software\Selenium_Python\chromedriver_win32\chromedriver.exe", desired_capabilities = chromeOptions.to_capabilities())
driver.implicitly_wait(5)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
time.sleep(2)
source_element = driver.find_element_by_xpath("//*[@id='box6']")
target_element = driver.find_element_by_xpath("//*[@id='box106']")
actions = ActionChains(driver)
time.sleep(2)
actions.drag_and_drop(source_element,target_element).perform()
time.sleep(2)
driver.quit()
