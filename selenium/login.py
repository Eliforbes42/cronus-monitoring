#login.py
#To run this,  $ python login.py $IP

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import sys

browser = webdriver.Firefox()
browser.get("http://%s/login" % sys.argv[1])  #**

time.sleep(10)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

# Type user:pass and submit
username.send_keys("admin")
password.send_keys("strongpassword")

login_attempt = browser.find_element_by_xpath("//*[@type=\"submit\"]")
login_attempt.click()
