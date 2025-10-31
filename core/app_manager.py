from pages.registration_page import RegistrationPage
from steps.registration import Registration

class ApplicationManager:
    def __init__(self):
        self.registration_page = RegistrationPage()
        self.registration = Registration()