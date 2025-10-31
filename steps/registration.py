import allure

from data.test_data import RegistrationData
from pages.registration_page import RegistrationPage

registration_page = RegistrationPage()

class Registration:

    def registration_as(self, registration_data: RegistrationData):
        (
            registration_page
            .open_registration_page()
            .first_name_fill(registration_data.first_name)
            .last_name_fill(registration_data.last_name)
            .user_email_fill(registration_data.email)
            .gender_fill(registration_data.gender_type)
            .user_number_fill(registration_data.number)
            .date_of_birth_fill(registration_data.date_of_birth)
            .subjects_fill(registration_data.subjects)
            .hobbies_fill(registration_data.hobbies)
            .picture_fill(registration_data.picture_url)
            .current_address_fill(registration_data.current_address)
            .state_fill(registration_data.state_type)
            .city_fill(registration_data.city_type)
            .submit()
        )
        return self

