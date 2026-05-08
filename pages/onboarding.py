# class OnboardingPage:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     # launch check
#     def is_app_launched(self):
#         return self.driver is not None
#
#     # click NEXT button
#     def click_next(self):
#         next_btn = self.driver.find_element(
#             "xpath",
#             '//android.widget.TextView[@text="Next"]'
#         )
#         next_btn.click()
#
#     # optional skip (if exists)
#     def click_skip(self):
#         try:
#             skip_btn = self.driver.find_element("id", "skip_button_id")
#             skip_btn.click()
#         except:
#             pass


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OnboardingPage:

    def __init__(self, driver):
        self.driver = driver

    def click_next(self):
        wait = WebDriverWait(self.driver, 10)
        next_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//android.widget.TextView[@text="Next"]')
            )
        )
        next_btn.click()
        print("button clicked")
        print("button clicked")