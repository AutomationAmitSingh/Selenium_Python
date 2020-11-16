import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(executable_path="D:\Software\Selenium_Python\chromedriver_win32\chromedriver.exe", desired_capabilities = chromeOptions.to_capabilities())
driver.implicitly_wait(5)
driver.get("https://www.expedia.com/")
driver.maximize_window()
driver.find_element(By.ID,"tab-flight-tab-hp").click()
time.sleep(2)
driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")
time.sleep(3)
driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYC")
driver.find_element(By.ID,"flight-departing-hp-flight").clear()
time.sleep(2)
driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("04/30/2019")
driver.find_element(By.ID,"flight-returning-hp-flight").clear()
time.sleep(2)
driver.find_element(By.ID,"flight-returning-hp-flight").send_keys("05/30/2019")
driver.find_element(By.XPATH,"//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()
wait = WebDriverWait(driver,10)
element=wait.until(ec.element_to_be_clickable((By.XPATH,"//*[@id='stopFilter_stops-0']")))
element.click()
#element = WebDriverWait(driver, 10).until(
       # ec.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-0']")))
#element.click()
time.sleep(2)
driver.quit()