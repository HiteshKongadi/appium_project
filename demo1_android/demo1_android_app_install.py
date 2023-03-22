import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that

des_cap = {
    "platformName": "android",
    "deviceName": "oneplus",
    "app": r"C:\Components\khan-academy-7-3-2.apk",
    "udid": "emulator-5554"
}

driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
driver.implicitly_wait(30)
driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
time.sleep(5)
driver.find_element(AppiumBy.XPATH, "//*[@text='Sign in']").click()
driver.find_element(AppiumBy.XPATH, "//*[@text='Sign in']").click()
driver.find_element(AppiumBy.XPATH, "//*[@text='Enter an e-mail address or username']").send_keys("xyz@abc.com")
driver.find_element(AppiumBy.XPATH, "//*[@text='Password']").send_keys("xyz@abc")
driver.find_element(AppiumBy.XPATH, "(//android.widget.TextView[@text='Sign in'])[2]").click()
actual_error = driver.find_element(AppiumBy.XPATH, "//*[@text='There was an issue signing in']").text
assert_that("There was an issue signing in").is_equal_to(actual_error)
time.sleep(5)
print(driver.page_source)

time.sleep(5)
driver.quit()
