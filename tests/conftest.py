from selene.support.shared import browser
import pytest

@pytest.fixture(scope='function', autouse=True)
def form_management():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.set_window_size(1920, 1080)
    yield
    browser.wait.for_(10)
    browser.quit()