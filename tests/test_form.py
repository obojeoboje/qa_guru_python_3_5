from selene.support.shared import browser
from selene import be, have
import os


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'attachments/photo.jpeg')


def test_filling_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Alexander')
    browser.element('#lastName').type('Oboje')
    browser.element('#userEmail').type('obojealexander@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type(9995204922)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select>[value="1999"]').click()
    browser.element('.react-datepicker__month-select>[value="4"]').click()
    browser.element('.react-datepicker__day--027').click()
    browser.element('#subjectsInput').type('Arts').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(file_path)
    browser.element('#currentAddress').type('Wall Street, 666')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Panipat').press_enter()
    browser.element('#submit').press_enter()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text('Alexander'
                                               and 'Oboje' and 'obojealexander@gmail.com'
                                               and 'Male' and '9995204922'
                                               and '27 May,1999' and 'Arts'
                                               and 'Sports' and 'Music'
                                               and 'photo.jpeg' and 'Wall Street, 666'
                                               and 'Haryana' and 'Panipat'))