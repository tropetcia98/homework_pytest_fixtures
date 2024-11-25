"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from homework_pytest_fxtures.pages.base_page import base_page
from selene import browser, have

desktop_only = pytest.mark.parametrize('browser_management', [(2560, 1440), (1920, 1080)], indirect=True)
mobile_only = pytest.mark.parametrize('browser_management', [(414, 736), (430, 932)], indirect=True)


@desktop_only
def test_github_desktop(browser_management):
    base_page.open_main_page()
    base_page.desktop_click_sign_in()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@mobile_only
def test_github_mobile(browser_management):
    base_page.open_main_page()
    base_page.mobile_click_sign_in()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
