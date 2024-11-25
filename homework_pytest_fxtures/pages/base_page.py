from selene import browser, have


class BasePage:

    def open_main_page(self):
        browser.open('/')

    def desktop_click_sign_in(self):
        browser.element('.HeaderMenu-link--sign-in').click()

    def mobile_click_sign_in(self):
        browser.all('.HeaderMenu-button').element_by(have.text('Sign in')).click()

    def should_be_visible_sign_in_button(self):
        browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


base_page = BasePage()
