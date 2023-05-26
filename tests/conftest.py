import pytest
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

# remove scope="class" to running fixture for every method
@pytest.fixture()
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    elif browser_name == "IE":
            driver = webdriver.Ie(executable_path=IEDriverManager().install())

    driver.delete_all_cookies()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            full_path = report.nodeid.replace("::", "_") + ".png"
            # full_path = 'tests/test_cases_icaps.py_TestFlow_test_temp[getData0].png'
            filename = full_path.split('/')[-1]  # to extract the last part after the last '/'
            _capture_screenshot(filename)
            if filename:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % filename
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

# def _capture_screenshot(name):
#         driver.get_screenshot_as_file(name)

def _capture_screenshot(name):
    path = os.path.join(os.getcwd(), 'reports', name)
    driver.get_screenshot_as_file(path)



