from selenium import webdriver
import time
from selenium.webdriver.common.by import By
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
driver=webdriver.Chrome(executable_path="D:\Software\Selenium_Python\chromedriver_win32\chromedriver.exe", desired_capabilities = chromeOptions.to_capabilities())
driver.implicitly_wait(5)
driver.get("https://seleniumhq.github.io/docs/api/java/index.html")
driver.maximize_window()
time.sleep(2)
driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("WebDriver").click()
driver.switch_to.default_content()
driver.switch_to.frame("classFrame")
driver.find_element_by_link_text("Depreciated")
driver.quit()