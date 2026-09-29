import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language: ru, en, fr, de, es, he")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language is None:
        raise pytest.UsageError("Please choose language using '--lanquage...' flag")
    print(f"\nstarting browser with '{user_language}' language...")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser...")
    time.sleep(5)
    browser.quit()