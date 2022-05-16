import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: ru, en, ... etc')


def pytest_configure():
    pytest.def_download_folder = 'C:\\Downloads\\Selenium_downloads'


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption('language')
    default_download_folder = {'download.default_directory': pytest.def_download_folder}

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('prefs',
                                        {'intl.accept_languages': user_language})
        options.add_experimental_option('prefs', default_download_folder)

        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)

        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="session", autouse=True)
def downloads_cleaner():
    yield
    print("\nclearing downloads folder")
    file_paths = os.listdir(pytest.def_download_folder)
    files_and_dirs = list(map(lambda name: os.path.join(pytest.def_download_folder, name), file_paths))

    for file in files_and_dirs:
        os.remove(file)
