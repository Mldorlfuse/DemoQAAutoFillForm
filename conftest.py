import pytest
from selenium import webdriver
from selene.support.shared import browser
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    # Настройки Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Без графического интерфейса
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Установка драйвера через WebDriver Manager

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager(version="114.0.5735.90").install()),
        options=chrome_options
    )

    # Настройка Selene
    browser.config.driver = driver
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 10

    yield browser

    driver.quit()