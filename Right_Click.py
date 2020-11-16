import time
from selenium import webdriver
from selenium.webdriver import ActionChains
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
driver=webdriver.Chrome(executable_path="D:\Software\Selenium_Python\chromedriver_win32\chromedriver.exe", desired_capabilities = chromeOptions.to_capabilities())
driver.implicitly_wait(5)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
time.sleep(2)
#button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
button = driver.find_element_by_xpath("//span[@class='context-menu-one btn btn-neutral']")
action = ActionChains(driver)
print("Before right click")
action.context_click(button).perform()
print("After right click")
time.sleep(2)
driver.quit()
