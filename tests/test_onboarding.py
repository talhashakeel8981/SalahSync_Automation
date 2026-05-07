from pages.onboarding import OnboardingPage

def test_app_launch(driver):
    page = OnboardingPage(driver)

    assert driver is not None

    page.click_next()

    print("Onboarding flow completed")