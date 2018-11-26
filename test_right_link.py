from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("путь/до/chromedriver")
driver.get("http://blog.csssr.ru/qa-engineer/")
monosnap_link = driver.find_element(By.XPATH, '//label[@for="soft"]').get_attribute("href")


class TestPageLinks(unittest.TestCase):

    def test_monosnap_link(self):
        self.assertEqual(monosnap_link, "http://monosnap.com/")

	driver.quit()


if __name__ == '__main__':
    unittest.main()