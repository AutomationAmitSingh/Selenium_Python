from selenium import webdriver
import pytest
import pytest_html

class TestOrangeHRM():

    @pytest.fixture()
    def setup(self):
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(executable_path="D:\Software\Selenium_Python\chromedriver_win32\chromedriver.exe",
                                  desired_capabilities=chromeOptions.to_capabilities())
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.close()

    def test_homePageTitle(self,setup):

        assert self.driver.title == "OrangeHRM"

    def test_login(self,setup):
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.title == "OrangeHRM"