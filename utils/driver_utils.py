from appium import webdriver
from appium.options.android import UiAutomator2Options

def create_driver():
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.platform_version = "16"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"

    options.app = "/Users/muhammadtalhashakeel/Salahsync/app/build/outputs/apk/debug/app-debug.apk"

    options.no_reset = False
    options.full_reset = False
    options.auto_grant_permissions = True

    options.new_command_timeout = 300

    return webdriver.Remote(
        command_executor="http://host.docker.internal:4723",
        options=options
    )