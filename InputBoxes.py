import time
from selenium import webdriver
from selenium.webdriver.common.by import By
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(executable_path="D:\Software\Selenium_Python\chromedriver_win32\chromedriver.exe", desired_capabilities = chromeOptions.to_capabilities())
driver.implicitly_wait(5)
driver.get("https://fs2.formsite.com/meherpavan/form2/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.NAME,"RESULT_TextField-1").click()
time.sleep(2)
numberInputBoxes = driver.find_elements(By.CLASS_NAME,"text_field")
print(len(numberInputBoxes))
driver.find_element(By.NAME,"RESULT_TextField-1").send_keys("Amit")
driver.find_element(By.NAME,"RESULT_TextField-2").send_keys("Singh")
driver.find_element(By.NAME,"RESULT_TextField-3").send_keys("99999999999")
Displayed = driver.find_element(By.NAME,"RESULT_TextField-3").is_displayed()
Enabled = driver.find_element(By.NAME,"RESULT_TextField-3").is_enabled()
Selected = driver.find_element(By.NAME,"RESULT_TextField-3").is_selected()
print("Element is displayed : "+str(Displayed))
print("Element is enabled : "+str(Enabled))
print("Element is selected : "+str(Selected))
driver.quit()
