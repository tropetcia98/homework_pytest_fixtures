"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have
from homework_pytest_fxtures.pages.base_page import base_page


def test_github_desktop(browser_management):
    if browser_management == 'mobile':
        pytest.skip(reason='Разрешение экрана - для мобильных устройств, поэтому тест пропущен')

    base_page.open_main_page()
    base_page.desktop_click_sign_in()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile(browser_management):
    base_page.open_main_page()
    base_page.mobile_click_sign_in()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
