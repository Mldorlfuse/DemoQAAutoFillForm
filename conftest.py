from selene import have, be
from selene.support.shared import browser
import pytest

@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    browser.config.base_url = 'https://demoqa.com'