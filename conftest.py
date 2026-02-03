import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )
    parser.addoption(
        "--url_name", action="store", default="https://rahulshettyacademy.com/client", help="server selection"
    )


@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param


@pytest.fixture
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    url_name = request.config.getoption("url_name")
    with sync_playwright() as p:
        if browser_name == "chrome":
            browser = p.chromium.launch(headless=True)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=True)

        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()
#2 times, 1st run opened browser and completed, homepage