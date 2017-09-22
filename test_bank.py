from selenium import webdriver
import logging
import time
from nose import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(filename="sample.log", level=logging.INFO,
                    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")


class bank():
    def __init__(self):
        self.driver = webdriver.Chrome("C:\chromedriver.exe")
        self.driver.implicitly_wait(30)

    def login(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

        try:
            self.driver.get(self.url)
            login_element = self.driver.find_element_by_xpath("//*[@name='uid']")
            login_element.send_keys(self.username)
            login_password = self.driver.find_element_by_xpath("//*[@name='password']")

            login_password.send_keys(self.password)
            login_button = self.driver.find_element_by_xpath(".//*[@name='btnLogin']")
            login_button.click()

            logging.info("Logging to Guru bank console")
            if self.driver.current_url == "http://www.demo.guru99.com/V4/manager/Managerhomepage.php":
                return self.driver
            else:
                return "Failed"



        except Exception as e:
            logging.error("Logging to openstack console failed")
            return "Failed"

    def logout(self):
        logout = self.driver.find_element_by_partial_link_text("Log out")
        logout.click()

        self.driver.close()

    def test_login_page(self):
        return self.driver.title()

    def close(self):
        self.driver.quit()


a1 = bank()


# a1.login("http://www.demo.guru99.com/V4/","mngr97869","AqaqAhu")
# a1.logout()

def test_correct_user_pass():
    assert "http://www.demo.guru99.com/V4/manager/Managerhomepage.php" == a1.login("http://www.demo.guru99.com/V4/",
                                                                                   "mngr97869", "AqaqAhu").current_url
    a1.close()


def test_wrong_user_correct_pass():
    assert "Failed" == a1.login("http://www.demo.guru99.com/V4/", "mngr97869", "AqaqA")
    a1.close()


def test_wrong_user_wrong_pass():
    assert "Failed" == a1.login("http://www.demo.guru99.com/V4/", "mngr97", "AqaqA")
    a1.close()


def test_correct_user_wrong_pass():
    assert "Failed" == a1.login("http://www.demo.guru99.com/V4/", "mng", "AqaqA")
    a1.close()











