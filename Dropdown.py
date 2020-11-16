import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
driver=webdriver.Chrome(executable_path="D:\Software\Selenium_Python\chromedriver_win32\chromedriver.exe", desired_capabilities = chromeOptions.to_capabilities())
driver.implicitly_wait(5)
driver.get("https://fs2.formsite.com/meherpavan/form2/")
driver.maximize_window()
time.sleep(2)
selectBox = driver.find_element_by_id("RESULT_RadioButton-7")
drp = Select(selectBox)
time.sleep(2)
drp.select_by_index(1)
time.sleep(2)
print(len(drp.options))
time.sleep(2)
all_options = drp.options
for option in all_options:
    print(option.text)
driver.quit()