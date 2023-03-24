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


class TestLogin(AppiumConfig):
    def test_invalid_login(self):
        """self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Enter an e-mail address or username']").send_keys(
            "xyz@abc.com")"""
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Dismiss")').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Sign in")').click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().descriptionContains("Enter an e-mail")').send_keys("xyz@abc.com")
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Password")').send_keys("admin234")
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Sign in").instance(1)').click()
        actual_error = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().textContains("an issue signing in")').text
        assert_that("There was an issue signing in").is_equal_to(actual_error)