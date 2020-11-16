import time
import cx_Oracle
from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver=webdriver.Chrome(executable_path="D:\Software\Selenium_Python\chromedriver_win32\chromedriver.exe", desired_capabilities = chromeOptions.to_capabilities())
driver.implicitly_wait(5)
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
time.sleep(2)

dsn_tns = cx_Oracle.makedsn('md1ta5bc', '1521', service_name='XE') #if needed, place an 'r' before any parameter in order to address any special character such as '\'.
conn = cx_Oracle.connect(user='system', password='Amit123', dsn=dsn_tns) #if needed, place an 'r' before any parameter in order to address any special character such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

c = conn.cursor()
c.execute('select * from Python_Oracle.authenticate') # use triple quotes if you want to spread your query across multiple lines
for row in c:
    print (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
    driver.find_element_by_name("userName").send_keys(row[0])
    time.sleep(1)
    driver.find_element_by_name("password").send_keys(row[1])
    time.sleep(1)
    driver.find_element_by_name("login").click()
    time.sleep(1)
    if driver.title == "Find a Flight: Mercury Tours:":
        print("Passed")
    else:
        print("Failed")
    driver.find_element_by_link_text("Home").click()



driver.quit()
c.close()
conn.close()

print("Test completed successfully")