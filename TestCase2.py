import unittest
from selenium import webdriver
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
#driver = webdriver.Chrome(executable_path="D:\Software\Selenium_Python\chromedriver_win32\chromedriver.exe",desired_capabilities=chromeOptions.to_capabilities())
#driver.implicitly_wait(5)

class SearchEngineTest(unittest.TestCase):




    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path="D:\Software\Selenium_Python\chromedriver_win32\chromedriver.exe",desired_capabilities=chromeOptions.to_capabilities())
        self.driver.get("https://www.google.com/")
        print(" Title of the page :"+self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="D:\Software\Selenium_Python\chromedriver_win32\chromedriver.exe",desired_capabilities=chromeOptions.to_capabilities())
        self.driver.get("https://bing.com/")
        print(" Title of the page :" + self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

