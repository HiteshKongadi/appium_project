import pytest
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
            "app": r"C:\Components\khan-academy-7-3-2.apk",
            "udid": "emulator-5554"
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",
                                       desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestAndroidDeviceCloud(AppiumConfig):

    def test_invalid_login(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        print(self.driver.page_source)

    def test_invalid_login_error(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Enter an e-mail address or username']").send_keys("xyz@abc.com")
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Password']").send_keys("xyz@abc")
        self.driver.find_element(AppiumBy.XPATH, "(//android.widget.TextView[@text='Sign in'])[2]").click()
        actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[@text='There was an issue signing in']").text
        assert_that("There was an issue signing in").is_equal_to(actual_error)

    def test_invalid_login_credentials(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
        self.driver.find_element(AppiumBy.XPATH,"//*[@content-desc='Settings']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Sign up with email']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='First name']").send_keys("XYZ")
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Last name']").send_keys("Lastname")
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Email address']").send_keys("XYZ@abc.com")
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Password']").send_keys("XYZ@abc")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Birthday']").click()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[1]").click()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[1]").clear()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[1]").send_keys("Aug")
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[2]").click()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[2]").clear()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[2]").send_keys("01")
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[3]").click()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[3]").clear()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[3]").send_keys("1995")
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='OK']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='CREATE']").click()
        actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Invalid password']").text
        assert_that("Invalid password").is_equal_to(actual_error)
        time.sleep(5)

