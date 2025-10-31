from typing import TypedDict


class DateOfBirth(TypedDict):
    day: str
    month: str
    year: str

class RegistrationData():
    first_name: str = 'Alex'
    last_name: str = 'Markov'
    email: str = 'test@test.ru'
    gender_type: str = '1'
    number: str = '1111111111'
    date_of_birth: DateOfBirth = {
        "day": '03',
        "month": 'September',
        "year": '1997'
    }
    subjects: str = 'Maths'
    hobbies: str = '1'
    picture_url: str = 'testImg.png'
    current_address: str = 'Test Address'
    state_type: str = '0'
    city_type: str = '0'
