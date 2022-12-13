from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def form_management():
    browser.config.base_url = 'https://demoqa.com'
    yield
    browser.quit()