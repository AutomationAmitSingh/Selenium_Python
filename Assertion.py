import unittest
from selenium import webdriver
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)

class Assertion(unittest.TestCase):

    def test_Google_Title(self):

        driver = webdriver.Chrome(executable_path="D:\Software\Selenium_Python\chromedriver_win32\chromedriver.exe",desired_capabilities=chromeOptions.to_capabilities())
        driver.get("https://www.google.com/")
        actualTitle = driver.title
        self.assertEqual("Google",actualTitle,"title is not same")
        self.assertNotEqual("Google123",actualTitle,"title are not equals")
        self.assertTrue(actualTitle=="Google")
        self.assertFalse(actualTitle=="Amit")
        value = None
        self.assertIsNone(value)
        self.assertIsNotNone(driver)
        list = {"python","selenium","java"}
        self.assertNotIn("Ruby",list)
        self.assertIn("java",list)
        self.assertGreater(100,10)
        self.assertGreaterEqual(10,10)
        self.assertLess(10,100)
        self.assertLessEqual(10,10)


if __name__ == "__main__":
    unittest.main()