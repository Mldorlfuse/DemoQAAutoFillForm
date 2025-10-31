import allure
from selene import have, be
from selene.support.shared import browser
from data.test_data import RegistrationData

from core.app_manager import ApplicationManager

app = ApplicationManager()
registration_data = RegistrationData()


@allure.feature("Регистрация")
@allure.story("Успешная регистрация")
def test_auto_fill_form(setup_browser):
    app.registration.registration_as(registration_data)

    # browser.element('#firstName').type('Alex')
    # browser.element('#lastName').type('Markov')
    # browser.element('#userEmail').type('test@test.ru')
    # browser.element('label[for="gender-radio-1"]').click()
    # browser.element('#userNumber').type('1111111111')
    # browser.element('#dateOfBirthInput').click()
    # month_select = browser.element(".react-datepicker__month-select").locate()
    # Select(month_select).select_by_visible_text("September")
    # year_select = browser.element(".react-datepicker__year-select").locate()
    # Select(year_select).select_by_visible_text("1997")
    # browser.element('.react-datepicker__day--003').click()
    # browser.element('#subjectsInput').type('Ma')
    # browser.all('.subjects-auto-complete__menu').element_by(have.text('Maths')).click()
    # browser.element('label[for=hobbies-checkbox-1]').click()
    # browser.element('#uploadPicture').send_keys(os.path.abspath('testImg.png'))
    # browser.element('#currentAddress').type('Test Address')
    # browser.element('#state').click()
    # browser.element('#react-select-3-option-0').click()
    # browser.element('#city').click()
    # browser.element('#react-select-4-option-0').click()
    # browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(be.visible)

    browser.all('.table-responsive tbody>tr')[0].all('td')[1].should(have.text('Alex Markov'))
    browser.all('.table-responsive tbody>tr')[1].all('td')[1].should(have.text('test@test.ru'))
    browser.all('.table-responsive tbody>tr')[2].all('td')[1].should(have.text('Male'))
    browser.all('.table-responsive tbody>tr')[3].all('td')[1].should(have.text('1111111111'))
    browser.all('.table-responsive tbody>tr')[4].all('td')[1].should(have.text('03 September,1997'))
    browser.all('.table-responsive tbody>tr')[5].all('td')[1].should(have.text('Maths'))
    browser.all('.table-responsive tbody>tr')[6].all('td')[1].should(have.text('Sports'))
    browser.all('.table-responsive tbody>tr')[7].all('td')[1].should(have.text('testImg.png'))
    browser.all('.table-responsive tbody>tr')[8].all('td')[1].should(have.text('Test Address'))
    browser.all('.table-responsive tbody>tr')[9].all('td')[1].should(have.text('NCR Delhi'))


