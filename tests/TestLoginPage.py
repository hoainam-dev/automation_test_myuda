import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_user_can_NOT_login_with_wrong_password(self):
        # Navigate to uda.edu.vn
        self.driver.get('https://my.uda.edu.vn/sv/svlogin')
        # Enter username = 'ytq@donga.edu.vn'

        userElement = self.driver.find_element(By.XPATH, '//input[@id="User"]')
        userElement.send_keys('54529')
        self.driver.save_screenshot('Step 1.png')

        passwordElement = self.driver.find_element(By.XPATH, '//input[@id="Password"]')
        passwordElement.send_keys('admin123')
        self.driver.save_screenshot('Step 2.png')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'Lnew1')
        loginBtnElement.click()

        # Check the error message 'Kiem tra lai ten dang nhap' appear
        errorMessageElement = self.driver.find_element(By.ID, 'Ltbao')
        self.driver.save_screenshot('Step 5.png')
        self.assertEqual(errorMessageElement.text, 'Kiểm tra lại tên hay password!')

    def test_user_can_login_with_true_password(self):
        # Navigate to uda.edu.vn
        self.driver.get('https://my.uda.edu.vn/sv/svlogin')
        # Enter username = 'ytq@donga.edu.vn'

        userElement = self.driver.find_element(By.XPATH, '//input[@id="User"]')
        userElement.send_keys('54529')
        self.driver.save_screenshot('Step 1.png')

        passwordElement = self.driver.find_element(By.XPATH, '//input[@id="Password"]')
        passwordElement.send_keys('huynhhoainam07112002')
        self.driver.save_screenshot('Step 2.png')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'Lnew1')
        loginBtnElement.click()

    def test_user_can_NOT_login_with_null_password_and_user(self):
        # Navigate to uda.edu.vn
        self.driver.get('https://my.uda.edu.vn/sv/svlogin')
        # Enter username = 'ytq@donga.edu.vn'

        userElement = self.driver.find_element(By.XPATH, '//input[@id="User"]')
        userElement.send_keys('')
        self.driver.save_screenshot('Step 1.png')

        passwordElement = self.driver.find_element(By.XPATH, '//input[@id="Password"]')
        passwordElement.send_keys('')
        self.driver.save_screenshot('Step 2.png')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'Lnew1')
        loginBtnElement.click()

        # Check the error message 'Kiem tra lai ten dang nhap' appear
        errorMessageElement = self.driver.find_element(By.ID, 'Ltbao')
        self.driver.save_screenshot('Step 5.png')
        self.assertEqual(errorMessageElement.text, 'Kiểm tra lại tên hay password! liên hệ ICT để được giúp đỡ')
        print("ok")
