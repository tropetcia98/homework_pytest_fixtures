"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser


@pytest.fixture(scope='function', params=[(2560, 1440), (1920, 1080), (1280, 720)])
def desktop_browser_management(request):
    browser.config.base_url = 'https://github.com/'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(scope='function', params=[(414, 736), (430, 932), (375, 812)])
def mobile_browser_management(request):
    browser.config.base_url = 'https://github.com/'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(scope='function', params=[(2560, 1440), (1920, 1080), (414, 736), (430, 932)])
def browser_management(request):
    browser.config.base_url = 'https://github.com/'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    if width >= 800:
        yield 'desktop'
    else:
        yield 'mobile'

    browser.quit()
