from selenium import webdriver
import unittest

driver = webdriver.Chrome("путь/до/chromedriver")
driver.get("http://blog.csssr.ru/qa-engineer/")
hr_link = driver.find_element_by_link_text("hr@csssr.com").get_attribute("href")
vk_link = driver.find_element_by_link_text("vk.com/csssr").get_attribute("href")

class TestPageLinks(unittest.TestCase):


    def test_hr_link(self):
        self.assertEqual(hr_link, "mailto:hr@csssr.com")

    def test_vk_link(self):
        self.assertEqual(vk_link, "http://vk.com/csssr")



driver.quit()



if __name__ == '__main__':
    unittest.main()