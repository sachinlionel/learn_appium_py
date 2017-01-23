from selenium import webdriver
import os
import unittest
from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['appium-version'] = '1.0'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['deviceName'] = 'AssPleaseWork'
desired_caps['app'] = os.path.abspath('/Users/SachIN/Downloads/app-niki-test.apk')
desired_caps['appActivity'] = 'com.nikiapp.LoginActivity'
print("setUp - Yes")


class Nikiests(unittest.TestCase):
    "Class to run tests against the Test app"

    def test_login_without_userid(self):
        "Managing to click Start button without user id"
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        startbutton = driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[1]")
        try:
            startbutton.click()
        except:
            chatwindow = driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.view.View[1]")
            if chatwindow:
                raise Exception("Test failed.")
                print("Login wihtout user id - Failed")
        print("Login wihtout user id should not happen - Yes")
        driver.quit()

    def test_Create_Profile_as_AlphaInput(self):
        "Managing to click Start button"
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        startbutton = driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[1]")
        editBox = driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]")
        try:
            editBox.send_keys("DumbMe")
            startbutton.click()
        except:
            chatwindow = driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.view.View[1]")
            if not chatwindow:
                raise Exception("Test failed.")
                print("Create Profile AlphaInput - Failed - As chatwindow doesnot appeared")
        print("Create Profile AlphaInput - Yes")
        driver.quit()

    def test_Create_Profile_as_NumericInput(self):
        "Managing to click Start button"
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        startbutton = driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[1]")
        editBox = driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]")
        try:
            editBox.send_keys("9986623505")
            startbutton.click()
        except:
            chatwindow = driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.view.View[1]")
            if not chatwindow:
                raise Exception("Test failed.")
                print("Create Profile NumericInput - Failed - As chatwindow doesnot appeared")
        print("Create Profile NumericInput - Yes")
        driver.quit()

    def test_Create_Profile_as_AlphaNumericInput(self):
        "Managing to click Start button"
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        startbutton = driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[1]")
        editBox = driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]")
        try:
            editBox.send_keys("99866Dumb")
            startbutton.click()
        except:
            chatwindow = driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.view.View[1]")
            if not chatwindow:
                raise Exception("Test failed.")
                print("Create Profile AlphaNunericInput - Failed - As chatwindow doesnot appeared")
        print("Create Profile AlphaNunericInput - Yes")
        driver.quit()




# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Nikiests)
    unittest.TextTestRunner(verbosity=1).run(suite)







