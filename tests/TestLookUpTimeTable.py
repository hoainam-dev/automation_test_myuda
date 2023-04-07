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

    def test_user_can_NOT_look_up_timetable_because_enter_wrong_information(self):
        # Navigate to my.uda.edu.vn
        self.driver.get('https://my.uda.edu.vn')

        # Enter username = '52053'
        userElement = self.driver.find_element(By.ID, 'User')
        userElement.send_keys('52053')

        # Enter password = '5555555555'
        passwordElement = self.driver.find_element(By.ID, 'Password')
        passwordElement.send_keys('5555555555')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'Lnew1')
        loginBtnElement.click()

        # Navigate to uda.edu.vn
        self.driver.get('https://my.uda.edu.vn/sv/timtkb')

        userElement = self.driver.find_element(By.ID, 'MainContent_Ttkb1')
        userElement.send_keys('TSHSN')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'MainContent_Lref1')
        loginBtnElement.click()

        # Check the error message 'Kiem tra lai ten dang nhap' appear
        errorMessageElement = self.driver.find_element(By.ID, 'MainContent_Panel6')
        self.assertEqual(errorMessageElement.text, 'Chưa tìm thấy thời khóa biểu!')

    def test_user_look_up_timetable(self):
        # Navigate to my.uda.edu.vn
        self.driver.get('https://my.uda.edu.vn')

        # Enter username = '52053'
        userElement = self.driver.find_element(By.ID, 'User')
        userElement.send_keys('52053')

        # Enter password = '5555555555'
        passwordElement = self.driver.find_element(By.ID, 'Password')
        passwordElement.send_keys('5555555555')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'Lnew1')
        loginBtnElement.click()

        # Navigate to uda.edu.vn
        self.driver.get('https://my.uda.edu.vn/sv/timtkb')

        userElement = self.driver.find_element(By.ID, 'MainContent_Ttkb1')
        userElement.send_keys('ST20A2A')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'MainContent_Lref1')
        loginBtnElement.click()
