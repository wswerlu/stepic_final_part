from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    # регистрируем пользователя
    def register_new_user(self, email, password):
        registration_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        registration_email.send_keys(email)
        registration_password_1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_1)
        registration_password_1.send_keys(password)
        registration_password_2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_2)
        registration_password_2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

    # проверяем страницу авторизации/регистрации
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # проверяем, что подстрока "login" есть в текущем url браузера
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Substring 'login' is not in url"

    # проверяем, что есть форма для авторизации
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    # проверяем, что есть форма для регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
