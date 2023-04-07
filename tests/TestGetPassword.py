import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # set a 10 second timeout for all driver commands
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_user_can_NOT_get_password_because_user_enter_wrong_information_Email(self):
        # Navigate to my.uda.edu.vn
        self.driver.get('https://my.uda.edu.vn')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'Lmiss')
        loginBtnElement.click()

        # Enter your email
        emailElement = self.driver.find_element(By.ID, 'TextBox1')
        emailElement.send_keys('nhan52053@donga.edu.vn')

        # Enter phone number
        phoneElement = self.driver.find_element(By.ID, 'TextBox2')
        phoneElement.send_keys('0855972850')

        # Enter your name
        phoneElement = self.driver.find_element(By.ID, 'TextBox3')
        phoneElement.send_keys('Nguyễn Ngọc Nhân')


        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'LinkButton1')
        loginBtnElement.click()

        errorMessageElement = self.driver.find_element(By.ID, 'Ltbao')
        self.assertEqual(errorMessageElement.text, 'Cơ sở không lưu đúng số liệu khai báo, liên hệ trung tâm ICT để giải quyết')

    def test_user_can_NOT_get_password_because_user_enter_wrong_information_phone_number(self):
        # Navigate to my.uda.edu.vn
        self.driver.get('https://my.uda.edu.vn')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'Lmiss')
        loginBtnElement.click()

        # Enter your email
        emailElement = self.driver.find_element(By.ID, 'TextBox1')
        emailElement.send_keys('nhannguyenvlog@gmail.com')

        # Enter phone number
        phoneElement = self.driver.find_element(By.ID, 'TextBox2')
        phoneElement.send_keys('0855972000')

        # Enter your name
        phoneElement = self.driver.find_element(By.ID, 'TextBox3')
        phoneElement.send_keys('Nguyễn Ngọc Nhân')


        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'LinkButton1')
        loginBtnElement.click()

        errorMessageElement = self.driver.find_element(By.ID, 'Ltbao')
        self.assertEqual(errorMessageElement.text, 'Cơ sở không lưu đúng số liệu khai báo, liên hệ trung tâm ICT để giải quyết')

    def test_user_can_NOT_get_password_because_user_enter_wrong_information_your_name(self):
        # Navigate to my.uda.edu.vn
        self.driver.get('https://my.uda.edu.vn')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'Lmiss')
        loginBtnElement.click()

        # Enter your email
        emailElement = self.driver.find_element(By.ID, 'TextBox1')
        emailElement.send_keys('nhannguyenvlog@gmail.com')

        # Enter phone number
        phoneElement = self.driver.find_element(By.ID, 'TextBox2')
        phoneElement.send_keys('0855972850')

        # Enter your name
        phoneElement = self.driver.find_element(By.ID, 'TextBox3')
        phoneElement.send_keys('Nguyễn Ngọc Nam')


        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'LinkButton1')
        loginBtnElement.click()

        errorMessageElement = self.driver.find_element(By.ID, 'Ltbao')
        self.assertEqual(errorMessageElement.text, 'Cơ sở không lưu đúng số liệu khai báo, liên hệ trung tâm ICT để giải quyết')