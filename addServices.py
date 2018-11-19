import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class admin_login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver

        driver.get("http://sujana.pythonanywhere.com/")
        time.sleep(1)

        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(1)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        assert "Logged In"
        time.sleep(2)


        # xpath, clicks on services button
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[3]/a").click()
        time.sleep(2)

        # xpath, clicks on add service button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        time.sleep(2)

        #fillig out the service form
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys("Bill Davis")
        time.sleep(1)
        elem = driver.find_element_by_id("id_service_category")
        elem.send_keys("Party Food")
        time.sleep(1)
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("We need party food for 100 people")
        time.sleep(1)

        elem = driver.find_element_by_id("id_location")
        elem.send_keys("UNO")
        time.sleep(1)
        elem = driver.find_element_by_id("id_service_charge")
        elem.send_keys("300")
        time.sleep(1)



        #xpath, clicks on save button for add service
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(2)

        # xpath, clicks on more option
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        time.sleep(2)
        # xpath, clicks on logout
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/ul/li[1]/a").click()
        time.sleep(2)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

