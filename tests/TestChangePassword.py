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
    def test_user_can_NOT_change_password_because_password_must_be_more_than_8_characters(self):
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
        self.driver.get('https://my.uda.edu.vn/sv/doipass')

        userElement = self.driver.find_element(By.ID, 'MainContent_TextBox1')
        userElement.send_keys('55555')

        passwordElement = self.driver.find_element(By.ID, 'MainContent_TextBox2')
        passwordElement.send_keys('55555')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'MainContent_Lnew1')
        loginBtnElement.click()

        errorMessageElement = self.driver.find_element(By.ID, 'MainContent_Label3')
        self.assertEqual(errorMessageElement.text, 'Passord có độ dài trên 8 ký tự!')

    def test_user_can_NOT_change_password_because_first_password_not_equals_password_confirm(self):
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
        self.driver.get('https://my.uda.edu.vn/sv/doipass')

        userElement = self.driver.find_element(By.ID, 'MainContent_TextBox1')
        userElement.send_keys('55555556')

        passwordElement = self.driver.find_element(By.ID, 'MainContent_TextBox2')
        passwordElement.send_keys('55555555')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'MainContent_Lnew1')
        loginBtnElement.click()

        errorMessageElement = self.driver.find_element(By.ID, 'MainContent_Label3')
        self.assertEqual(errorMessageElement.text, 'Passord có độ dài trên 8 ký tự!')

    def test_user_can_NOT_change_password_because_password_is_not_null(self):
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
        self.driver.get('https://my.uda.edu.vn/sv/doipass')

        userElement = self.driver.find_element(By.ID, 'MainContent_TextBox1')
        userElement.send_keys('')

        passwordElement = self.driver.find_element(By.ID, 'MainContent_TextBox2')
        passwordElement.send_keys('')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'MainContent_Lnew1')
        loginBtnElement.click()

        errorMessageElement = self.driver.find_element(By.ID, 'MainContent_Label3')
        self.assertEqual(errorMessageElement.text, 'Passord có độ dài trên 8 ký tự!')

    def test_user_change_password_successfully(self):
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
        self.driver.get('https://my.uda.edu.vn/sv/doipass')

        userElement = self.driver.find_element(By.ID, 'MainContent_TextBox1')
        userElement.send_keys('55555555')

        passwordElement = self.driver.find_element(By.ID, 'MainContent_TextBox2')
        passwordElement.send_keys('55555555')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'MainContent_Lnew1')
        loginBtnElement.click()

# if __name__ == '__main__':
#     unittest.main()