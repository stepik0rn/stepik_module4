import pytest
from importlib import import_module


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name', 
        action='store', 
        default="chrome",
        help="Choose a browser: chrome or firefox"
    )
    parser.addoption(
        '--language', 
        action='store', 
        default="en",
        help="Choose abrowser: chrome or firefox"
    )

    
@pytest.fixture(scope="function")
def browser(request):
    browser_name = (request.config.getoption("browser_name") or '').lower()
    print(browser_name)
    language = request.config.getoption("language")

    if browser_name not in ["chrome", "firefox"]:
        raise pytest.UsageError(f"Unknown browser '{browser_name}' specified.")
    options = getattr(import_module(f'selenium.webdriver.{browser_name}.options'), "Options")()
    Browser = getattr(import_module(f'selenium.webdriver'), browser_name.capitalize())

    if browser_name == "chrome":
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
    elif browser_name == "firefox":
        options.set_preference("intl.accept_languages", language)

    browser = Browser(options=options)
    browser.implicitly_wait(30)
    print("\nStart browser for test..")
    yield browser
    print("\nQuit browser..")
    browser.quit()
