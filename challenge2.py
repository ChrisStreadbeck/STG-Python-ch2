import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver.exe')

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        searchterm = "exotic"
        print ('go to google')
        self.driver.get("https://www.copart.com")
        searchfield = self.driver.find_element(By.ID, "input-search")
        searchfield.send_keys("exotic")
        searchfield.send_keys(Keys.ENTER)

        dataelement = self.driver.find_element(By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody")
        html = dataelement.get_attribute("innerHTML")
        self.assertIn("PORSCHE", html)


if __name__ == '__main__':
    unittest.main()
