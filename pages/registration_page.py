import allure
from selene import browser, have
import os
from selenium.webdriver.support.ui import Select

class RegistrationPage:
    url_page = '/automation-practice-form'
    first_name_field = browser.element('#firstName')
    last_name_field = browser.element('#lastName')
    user_email_field = browser.element('#userEmail')
    gender_field = browser.element('#genterWrapper')
    user_number_field = browser.element('#userNumber')
    date_of_birth_block = browser.element('#dateOfBirth')
    date_of_birth_field = browser.element('#dateOfBirthInput')
    month_date_of_birth_field = browser.element('.react-datepicker__month-select')
    year_date_of_birth_field = browser.element('.react-datepicker__year-select')
    subjects_field = browser.element('#subjectsInput')
    subjects_menu_field = browser.all('.subjects-auto-complete__menu')
    hobbies_wrapper = browser.element('#hobbiesWrapper')
    picture_field = browser.element('#uploadPicture')
    current_address_field = browser.element('#currentAddress')
    state_wrapper = browser.element('#state')
    city_wrapper = browser.element('#city')
    submit_button = browser.element('#submit')

    @allure.step(f"Открыть страницу {url_page}")
    def open_registration_page(self):
        browser.open(self.url_page)
        return self

    def first_name_fill(self, first_name: str):
        with allure.step(f"Ввести в поле first name значение {first_name}"):
            self.first_name_field.type(first_name)
            return self

    def last_name_fill(self, last_name: str):
        self.last_name_field.type(last_name)
        return self

    def user_email_fill(self, email: str):
        self.user_email_field.type(email)
        return self

    def gender_fill(self, gender_type: str):
        self.gender_field.element(f'label[for="gender-radio-{gender_type}"]').click()
        return self

    def user_number_fill(self, user_number: str):
        self.user_number_field.type(user_number)
        return self

    def date_of_birth_fill(self, date_of_birth: dict):
        self.date_of_birth_field.click()
        month_select = self.month_date_of_birth_field.locate()
        Select(month_select).select_by_visible_text(date_of_birth['month'])
        year_select = self.year_date_of_birth_field.locate()
        Select(year_select).select_by_visible_text(date_of_birth['year'])
        self.date_of_birth_block.element(f".react-datepicker__day--0{date_of_birth['day']}").click()
        return self

    def subjects_fill(self, subjects_name: str):
        self.subjects_field.type(subjects_name)
        self.subjects_menu_field.element_by(have.text(subjects_name)).click()
        return self

    def hobbies_fill(self, hobbies_type: str):
        self.hobbies_wrapper.element(f'label[for=hobbies-checkbox-{hobbies_type}]').click()
        return self

    def picture_fill(self, picture_url: str):
        self.picture_field.send_keys(os.path.abspath(picture_url))
        return self

    def current_address_fill(self, address: str):
        self.current_address_field.type(address)
        return self

    def state_fill(self, state_type: str):
        self.state_wrapper.click()
        browser.element(f'#react-select-3-option-{state_type}').click()
        return self

    def city_fill(self, city_type: str):
        self.city_wrapper.click()
        browser.element(f'#react-select-4-option-{city_type}').click()
        return self

    def submit(self):
        self.submit_button.click()
        return self