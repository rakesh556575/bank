from selenium import webdriver
import logging
import time
from nose import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
logging.basicConfig(filename="sample.log", level=logging.INFO,format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")


class bank():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path="C:\geckodriver-v0.18.0-win64\geckodriver.exe")
        self.driver.implicitly_wait(10)

    def login(self,url,username,password):
        self.url=url
        self.username=username
        self.password=password
        self.driver.get(self.url)
        try:
            login_element = self.driver.find_element_by_xpath("//*[@name='uid']")
            login_element.send_keys(self.username)
            login_password = self.driver.find_element_by_xpath("//*[@name='password']")

            login_password.send_keys(self.password)
            login_button = self.driver.find_element_by_xpath(".//*[@name='btnLogin']")
            login_button.click()


            logging.info("Logging to Guru bank console")
            return self.driver.current_url



        except Exception as e:
            logging.error("Logging to openstack console failed")
            print("Execption occured {}".format(e))


    def logout(self):
        logout=self.driver.find_element_by_partial_link_text("Log out")
        logout.click()


        self.driver.close()

    def test_login_page(self):
        return self.driver.title()


#a1=bank()
#a1.login("http://www.demo.guru99.com/V4/","mngr97869","AqaqAhu")
#a1.logout()

def test():
    assert "http://www.demo.guru99.com/V4/index.php"==a1.login("http://www.demo.guru99.com/V4/","mngr97869","AqaqAhu")








