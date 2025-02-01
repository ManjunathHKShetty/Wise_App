import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request, browser):
    if browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")

@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "Wise Automation"

@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.append(f"Project: Wise")
    prefix.append(f"Module: Auto")
    prefix.append(f"Tester: Manjunath HK")


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)














