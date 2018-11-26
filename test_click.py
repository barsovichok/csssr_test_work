from selenium import webdriver
import unittest

driver = webdriver.Chrome("путь/до/chromedriver")
driver.get("http://blog.csssr.ru/qa-engineer/")
click_bug = driver.find_element_by_class_name("bug").click()
driver.quit()



if __name__ == '__main__':
    unittest.main()