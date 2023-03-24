import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

"""Automation using ANDROID_UIAUTOMATOR"""


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
            # "app": r"C:\Components\khan-academy-7-3-2.apk",
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestMessages(AppiumConfig):
    def test_list_sms(self):
        if len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

        messges = self.driver.execute_script("mobile:listSms", {"max": 2})
        print(messges)
