import time
import XLUtils
from selenium import webdriver
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
driver=webdriver.Chrome(executable_path="D:\Software\Selenium_Python\chromedriver_win32\chromedriver.exe", desired_capabilities = chromeOptions.to_capabilities())
driver.implicitly_wait(5)
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
time.sleep(2)
path = "Login.xlsx"
rows = XLUtils.getRowCount(path, 'Sheet1')
for r in range(2, rows+1):
    userName = XLUtils.readData(path, 'Sheet1', r, 1)
    password = XLUtils.readData(path, 'Sheet1', r, 2)

    driver.find_element_by_name("userName").send_keys(userName)
    driver.find_element_by_name("password").send_keys(password)

    driver.find_element_by_name("login").click()
    if driver.title == "Find a Flight : Mercury Tours:":
        print("Passed")
        XLUtils.writeData(path, 'Sheet1', r, 3, "Passed")
    else:
        print("Failed")
        XLUtils.writeData(path, 'Sheet1', r, 3, "Failed")

        driver.find_element_by_link_text("Home").click()

driver.quit()

