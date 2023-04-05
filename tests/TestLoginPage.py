import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    # Testcase 01
    def test_user_can_login_with_true_password(self):
        # Navigate to uda.edu.vn
        self.driver.get('https://my.uda.edu.vn/sv/svlogin')
        # Enter username = 'ytq@donga.edu.vn'

        userElement = self.driver.find_element(By.XPATH, '//input[@id="User"]')
        userElement.send_keys('54529')
        self.driver.save_screenshot('TC01 Step 1.png')

        passwordElement = self.driver.find_element(By.XPATH, '//input[@id="Password"]')
        passwordElement.send_keys('huynhhoainam07112002')
        self.driver.save_screenshot('TC01 Step 2.png')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'Lnew1')
        loginBtnElement.click()

    # Testcase 02
    def test_user_can_NOT_login_with_wrong_password(self):
        # Navigate to uda.edu.vn
        self.driver.get('https://my.uda.edu.vn/sv/svlogin')
        # Enter username = 'ytq@donga.edu.vn'

        userElement = self.driver.find_element(By.XPATH, '//input[@id="User"]')
        userElement.send_keys('54529')
        self.driver.save_screenshot('TC02 Step 1.png')

        passwordElement = self.driver.find_element(By.XPATH, '//input[@id="Password"]')
        passwordElement.send_keys('admin123')
        self.driver.save_screenshot('TC02 Step 2.png')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'Lnew1')
        loginBtnElement.click()

        # Check the error message 'Kiem tra lai ten dang nhap' appear
        errorMessageElement = self.driver.find_element(By.ID, 'Ltbao')
        self.driver.save_screenshot('TC02 Step 5.png')
        self.assertEqual(errorMessageElement.text, 'Kiểm tra lại tên hay password!')

    # Testcase 03
    def test_user_can_NOT_login_with_special_user(self):
        # Navigate to uda.edu.vn
        self.driver.get('https://my.uda.edu.vn/sv/svlogin')
        # Enter username = 'ytq@donga.edu.vn'

        userElement = self.driver.find_element(By.XPATH, '//input[@id="User"]')
        userElement.send_keys('#@$%&*({')
        self.driver.save_screenshot('TC03 Step 1.png')

        passwordElement = self.driver.find_element(By.XPATH, '//input[@id="Password"]')
        passwordElement.send_keys('')
        self.driver.save_screenshot('TC03 Step 2.png')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'Lnew1')
        loginBtnElement.click()

        # Check the error message 'Kiem tra lai ten dang nhap' appear
        errorMessageElement = self.driver.find_element(By.ID, 'Ltbao')
        self.driver.save_screenshot('TC03 Step 5.png')
        self.assertEqual(errorMessageElement.text, 'Kiểm tra lại tên hay password! liên hệ ICT để được giúp đỡ')

    # Testcase 04
    def test_user_can_NOT_login_with_special_password(self):
        # Navigate to uda.edu.vn
        self.driver.get('https://my.uda.edu.vn/sv/svlogin')
        # Enter username = 'ytq@donga.edu.vn'

        userElement = self.driver.find_element(By.XPATH, '//input[@id="User"]')
        userElement.send_keys('54529')
        self.driver.save_screenshot('TC04 Step 1.png')

        passwordElement = self.driver.find_element(By.XPATH, '//input[@id="Password"]')
        passwordElement.send_keys('#@$%&*({')
        self.driver.save_screenshot('TC04 Step 2.png')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'Lnew1')
        loginBtnElement.click()

        # Check the error message 'Kiem tra lai ten dang nhap' appear
        errorMessageElement = self.driver.find_element(By.ID, 'Ltbao')
        self.driver.save_screenshot('TC04 Step 5.png')
        self.assertEqual(errorMessageElement.text, 'Kiểm tra lại tên hay password!')

    # Testcase 05
    def test_user_can_NOT_login_with_null_user(self):
        # Navigate to uda.edu.vn
        self.driver.get('https://my.uda.edu.vn/sv/svlogin')
        # Enter username = 'ytq@donga.edu.vn'

        userElement = self.driver.find_element(By.XPATH, '//input[@id="User"]')
        userElement.send_keys('')
        self.driver.save_screenshot('TC05 Step 1.png')

        passwordElement = self.driver.find_element(By.XPATH, '//input[@id="Password"]')
        passwordElement.send_keys('12345678')
        self.driver.save_screenshot('TC05 Step 2.png')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'Lnew1')
        loginBtnElement.click()

        # Check the error message 'Kiem tra lai ten dang nhap' appear
        errorMessageElement = self.driver.find_element(By.ID, 'Ltbao')
        self.driver.save_screenshot('TC05 Step 5.png')
        self.assertEqual(errorMessageElement.text, 'Kiểm tra lại tên hay password! liên hệ ICT để được giúp đỡ')

    # Testcase 06
    def test_user_can_NOT_login_with_null_password(self):
        # Navigate to uda.edu.vn
        self.driver.get('https://my.uda.edu.vn/sv/svlogin')
        # Enter username = 'ytq@donga.edu.vn'

        userElement = self.driver.find_element(By.XPATH, '//input[@id="User"]')
        userElement.send_keys('54529')
        self.driver.save_screenshot('TC06 Step 1.png')

        passwordElement = self.driver.find_element(By.XPATH, '//input[@id="Password"]')
        passwordElement.send_keys('')
        self.driver.save_screenshot('TC06 Step 2.png')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'Lnew1')
        loginBtnElement.click()

        # Check the error message 'Kiem tra lai ten dang nhap' appear
        errorMessageElement = self.driver.find_element(By.ID, 'Ltbao')
        self.driver.save_screenshot('TC06 Step 5.png')
        self.assertEqual(errorMessageElement.text, 'Kiểm tra lại tên hay password! liên hệ ICT để được giúp đỡ')

    # Testcase 07
    def test_user_can_NOT_login_with_null_password_and_user(self):
        # Navigate to uda.edu.vn
        self.driver.get('https://my.uda.edu.vn/sv/svlogin')
        # Enter username = 'ytq@donga.edu.vn'

        userElement = self.driver.find_element(By.XPATH, '//input[@id="User"]')
        userElement.send_keys('')
        self.driver.save_screenshot('TC07 Step 1.png')

        passwordElement = self.driver.find_element(By.XPATH, '//input[@id="Password"]')
        passwordElement.send_keys('')
        self.driver.save_screenshot('TC07 Step 2.png')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'Lnew1')
        loginBtnElement.click()

        # Check the error message 'Kiem tra lai ten dang nhap' appear
        errorMessageElement = self.driver.find_element(By.ID, 'Ltbao')
        self.driver.save_screenshot('TC07 Step 5.png')
        self.assertEqual(errorMessageElement.text, 'Kiểm tra lại tên hay password! liên hệ ICT để được giúp đỡ')

    # Testcase 08
    def test_function_forgot_password_with_valid_information(self):
        # Navigate to uda.edu.vn
        self.driver.get('https://my.uda.edu.vn/sv/svlogin')
        # Enter username = 'ytq@donga.edu.vn'

        # Click on forgot password button
        loginBtnElement = self.driver.find_element(By.ID, 'Lmiss')
        loginBtnElement.click()

        emailElement = self.driver.find_element(By.XPATH, '//input[@id="TextBox1"]')
        emailElement.send_keys('hoainamadm@gmail.com')
        self.driver.save_screenshot('TC08 Step 2.png')

        phoneElement = self.driver.find_element(By.XPATH, '//input[@id="TextBox2"]')
        phoneElement.send_keys('0375851697')
        self.driver.save_screenshot('TC08 Step 3.png')

        nameElement = self.driver.find_element(By.XPATH, '//input[@id="TextBox3"]')
        nameElement.send_keys('Huỳnh Hoài Nam')
        self.driver.save_screenshot('TC08 Step 4.png')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'LinkButton1')
        loginBtnElement.click()

        # Check the error message 'Kiem tra lai ten dang nhap' appear
        errorMessageElement = self.driver.find_element(By.ID, 'Ltbao')
        self.driver.save_screenshot('TC08 Step 6.png')
        self.assertEqual(errorMessageElement.text, 'Password vừa được chuyển đến mail của bạn, Vui lòng mở email và đăng nhập...')

    # Testcase 09
    def test_function_forgot_password_with_invalid_information(self):
        # Navigate to uda.edu.vn
        self.driver.get('https://my.uda.edu.vn/sv/svlogin')
        # Enter username = 'ytq@donga.edu.vn'

        # Click on forgot password button
        loginBtnElement = self.driver.find_element(By.ID, 'Lmiss')
        loginBtnElement.click()

        emailElement = self.driver.find_element(By.XPATH, '//input[@id="TextBox1"]')
        emailElement.send_keys('admin@gmail.com')
        self.driver.save_screenshot('TC09 Step 2.png')

        phoneElement = self.driver.find_element(By.XPATH, '//input[@id="TextBox2"]')
        phoneElement.send_keys('0123456789')
        self.driver.save_screenshot('TC09 Step 3.png')

        nameElement = self.driver.find_element(By.XPATH, '//input[@id="TextBox3"]')
        nameElement.send_keys('Admin')
        self.driver.save_screenshot('TC09 Step 4.png')

        # Click on login button
        loginBtnElement = self.driver.find_element(By.ID, 'LinkButton1')
        loginBtnElement.click()

        # Check the error message 'Kiem tra lai ten dang nhap' appear
        errorMessageElement = self.driver.find_element(By.ID, 'Ltbao')
        self.driver.save_screenshot('TC09 Step 6.png')
        self.assertEqual(errorMessageElement.text, 'Vui lòng kiểm tra lại các thông tin đã nhập!')