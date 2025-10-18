from selene import browser, have, be
from selenium.webdriver.support.ui import Select
import os

browser.config.base_url = "https://demoqa.com"

def test_auto_fill_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Alex')
    browser.element('#lastName').type('Markov')
    browser.element('#userEmail').type('test@test.ru')
    browser.element('#gender-radio-1').click()
    browser.element('#userNumber').type('1111111111')
    browser.element('#dateOfBirthInput').click()
    selectMonth = Select(browser.element('.react-datepicker__month-dropdown-container').locate())
    selectMonth.select_by_visible_text('September')
    selectYear = Select(browser.element('.react-datepicker__year-dropdown-container').locate())
    selectYear.select_by_visible_text('1997')
    browser.all('.react-datepicker__month').element_by(have.text('3')).click()
    browser.element('#subjectsInput').type('Ma')
    browser.element('.subjects-auto-complete__menu').element_by(have.text('Maths')).click()
    browser.element('#hobbies-checkbox-1').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('testImg.png'))
    browser.element('#currentAddress').type('Test Address')
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(be.visible)

