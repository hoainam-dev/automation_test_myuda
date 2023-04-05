import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def loginSuccess(self):
    # Navigate to my.uda.edu.vn
    self.driver.get('https://my.uda.edu.vn')

    # Enter username = '52437'
    userElement = self.driver.find_element(By.ID, 'User')
    userElement.send_keys('52437')

    # Enter password = '3000212383'
    passwordElement = self.driver.find_element(By.ID, 'Password')
    passwordElement.send_keys('0862567721')

    # Click on login button
    loginBtnElement = self.driver.find_element(By.ID, 'Lnew1')
    loginBtnElement.click()
    self.driver.save_screenshot('Step 1.png')
    #Login success
    expected_url = 'https://my.uda.edu.vn/sv/cthoc'
    assert self.driver.current_url == expected_url
    print('Login Success!')

#Input Profile
def input(self ,id ,text):
    inputElement = self.driver.find_element(By.ID, id)
    inputElement.clear()
    inputElement.send_keys(text)

#clickProfile
def profile(self):
    #Profile
    BtnNav = self.driver.find_element(By.ID, 'Image1')
    BtnNav.click()
    #btnUpdate(Sửa)
    BtnNav = self.driver.find_element(By.ID, 'MainContent_FV2_Lsua1')
    BtnNav.click()
#clickChangePassword
def changePassword(self, id, context):
    #find input changePassword worng pass
    ElementChangePassword = self.driver.find_element(By.ID, id)
    ElementChangePassword.send_keys(context)

    #find button changpassword
    btnChangePassword = self.driver.find_element(By.ID, 'MainContent_Lrefesh')
    btnChangePassword.click()

#Input Change Password In Profile

def inputChangePassword(self, inputPassword, AgainInputPassword):
    #find input Element changePassword
    ElementInputChangePassword = self.driver.find_element(By.ID, 'MainContent_Tpass')
    ElementInputChangePassword.send_keys(inputPassword)

    ElementAgainInputPassword = self.driver.find_element(By.ID, 'MainContent_Tnlp')
    ElementAgainInputPassword.send_keys(AgainInputPassword)

    #Btn ChangePassword
    BtnChangePassword = self.driver.find_element(By.ID, 'MainContent_Ldo')
    BtnChangePassword.click()

#Check the error message 'Kiểm tra lại yêu cầu password ' appear
def checkERRORS(self, photo, myErrorMessage):
    errorMessageElement = self.driver.find_element(By.ID, 'MainContent_Ltbc')
    self.driver.save_screenshot(photo)
    my_string = myErrorMessage
    encoded_string = my_string.encode("utf-8")
    self.assertEqual(errorMessageElement.text.encode("utf-8"), encoded_string)

class MyTestCase(unittest.TestCase):

    def setUp(self):
        driver_service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=driver_service)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_TC01_homepage(self):
        loginSuccess(self)



    def test_TC02(self):
        #nav my.uda.edu.vn/home
        loginSuccess(self)

        #Profile
        profile(self)

        #input CCCD BUG INPUT TEXT
        input(self, 'MainContent_FV2_TextBox19', 'Nam Pro')

        #input Phone1 BUG INPUT TEXT
        input(self, 'MainContent_FV2_TextBox6', 'Nam Pro')

        #input email BUG INPUT Ky Tu Dat Biet
        input(self, 'MainContent_FV2_TextBox7', '##$:>>>')
        self.driver.save_screenshot('Step 2.png')
        #input telSos BUG INPUT TEXT
        input(self, 'MainContent_FV2_TextBox9', 'Nam Pro')

        #input phone2 BUG INPUT TEXT
        input(self, 'MainContent_FV2_TextBox15', 'Nam Pro')

        #input phone3 BUG INPUT TEXT
        input(self, 'MainContent_FV2_TextBox18', 'Nam Pro')

        #Submit
        BtnSubmitUpdata = self.driver.find_element(By.ID, 'MainContent_FV2_Lu2')
        BtnSubmitUpdata.click()
        self.driver.save_screenshot('Step 3.png')

    def test_TC03(self):
        #nav my.uda.edu.vn/home
        loginSuccess(self)

        #Profile
        profile(self)

        #input CCCD BUG INPUT KTDD
        input(self, 'MainContent_FV2_TextBox19', '@#$!!Nam0411')

        #input Phone1 BUG INPUT TEXT, KTDD, TRIM
        input(self, 'MainContent_FV2_TextBox6', 'Nam Pro@@### 0 7 4 4')

        #input email BUG INPUT Sai Dinh Dang
        input(self, 'MainContent_FV2_TextBox7', '@nam@gmail@.com12!')
        self.driver.save_screenshot('Step 4.png')
        #input telSos BUG INPUT TEXT, KTDD, TRIM
        input(self, 'MainContent_FV2_TextBox9', 'Nam Pro@@### 0 7 4 4')

        #input phone2 BUG INPUT TEXT
        input(self, 'MainContent_FV2_TextBox15', 'Nam Pro@@### 0 7 4 4')

        #input phone3 BUG INPUT TEXT
        input(self, 'MainContent_FV2_TextBox18', 'Nam Pro@@### 0 7 4 4')

        #Submit
        BtnSubmitUpdata = self.driver.find_element(By.ID, 'MainContent_FV2_Lu2')
        BtnSubmitUpdata.click()
        self.driver.save_screenshot('Step 5.png')

    def test_TC04(self):
        #nav my.uda.edu.vn/home
        loginSuccess(self)

        #Profile
        profile(self)

        #input CCCD BUG INPUT >12 so
        input(self, 'MainContent_FV2_TextBox19', '1223456789123456789')

        #input Phone1 BUG INPUT  >10 so
        input(self, 'MainContent_FV2_TextBox6', '12345678912345679')

        #input email BUG INPUT Sai Dinh Dang, TRIM
        input(self, 'MainContent_FV2_TextBox7', 'nam nam@gmail.com')
        self.driver.save_screenshot('Step 6.png')
        #input telSos BUG INPUT >10 so
        input(self, 'MainContent_FV2_TextBox9', '12345678912345679')

        #input phone2 BUG INPUT >10 so
        input(self, 'MainContent_FV2_TextBox15', '12345678912345679')

        #input phone3 BUG INPUT >10 so
        input(self, 'MainContent_FV2_TextBox18', '12345678912345679')
        #Submit
        BtnSubmitUpdata = self.driver.find_element(By.ID, 'MainContent_FV2_Lu2')
        BtnSubmitUpdata.click()
        self.driver.save_screenshot('Step 7.png')

    def test_TC05(self):
        #nav my.uda.edu.vn/home
        loginSuccess(self)

        #Profile
        profile(self)

        #input CCCD BUG INPUT >12 so
        input(self, 'MainContent_FV2_TextBox19', ':)')

        #input Phone1 BUG INPUT  >10 so
        input(self, 'MainContent_FV2_TextBox6', '--)')

        #input email BUG INPUT Sai Dinh Dang, TRIM
        input(self, 'MainContent_FV2_TextBox7', '00>>>')
        self.driver.save_screenshot('Step 8.png')
        #input telSos BUG INPUT >10 so
        input(self, 'MainContent_FV2_TextBox9', '####')

        #input phone2 BUG INPUT >10 so
        input(self, 'MainContent_FV2_TextBox15', 'admin@@!,,nam')

        #input phone3 BUG INPUT >10 so
        input(self, 'MainContent_FV2_TextBox18', 'admin@@!,,nam')
        #Submit
        BtnSubmitUpdata = self.driver.find_element(By.ID, 'MainContent_FV2_Lu2')
        BtnSubmitUpdata.click()
        self.driver.save_screenshot('Step 9.png')

    def test_TC06_user_NOT_ChangePassword_in_Profile(self):
        #nav my.uda.edu.vn/home
        loginSuccess(self)

        #Profile my.uda.edu.vn/sv/thongtinsv
        profile(self)

        changePassword(self, 'MainContent_Tptd', '3000212383')

        #Check the error message 'Password chưa đúng, vui lòng liên hệ trung tâm ICT' appear
        errorMessageElement = self.driver.find_element(By.ID, 'MainContent_Ltbc')
        self.driver.save_screenshot('Step 10.png')
        my_string = "Password chưa đúng, vui lòng liên hệ trung tâm ICT"
        encoded_string = my_string.encode("utf-8")
        self.assertEqual(errorMessageElement.text.encode("utf-8"), encoded_string)

    def test_TC07_user_NOT_ChangePassword_in_Profile(self):
        #nav my.uda.edu.vn/home
        loginSuccess(self)

        #Profile my.uda.edu.vn/sv/thongtinsv
        profile(self)

        #CHECK CURRENT PASSWORD -> PASSWORD ĐÚNG
        changePassword(self, 'MainContent_Tptd', '0862567721')

        #TEST ĐỔI PASSWORD -> 2 MK Khong giống nhau
        inputChangePassword(self, '3000212383', '3000212382')

        #Check the error message 'Password chưa đúng, vui lòng liên hệ trung tâm ICT' appear
        errorMessageElement = self.driver.find_element(By.ID,'MainContent_Ltbc')
        self.driver.save_screenshot('Step 11.png')
        my_string = "Kiểm tra lại yêu cầu password"
        encoded_string = my_string.encode("utf-8")
        self.assertEqual(errorMessageElement.text.encode("utf-8"), encoded_string)
    def test_TC08_user_NOT_ChangePassword_in_Profile(self):
        #nav my.uda.edu.vn/home
        loginSuccess(self)

        #Profile my.uda.edu.vn/sv/thongtinsv
        profile(self)

        #CHECK CURRENT PASSWORD -> PASSWORD ĐÚNG
        changePassword(self, 'MainContent_Tptd', '0862567721')

        #TEST ĐỔI PASSWORD -> 2 MK Khong giống nhau trim
        inputChangePassword(self, '3000212383', '30 00212383')

        #Check the error message 'Password chưa đúng, vui lòng liên hệ trung tâm ICT' appear
        errorMessageElement = self.driver.find_element(By.ID,'MainContent_Ltbc')
        self.driver.save_screenshot('Step 12.png')
        my_string = "Kiểm tra lại yêu cầu password"
        encoded_string = my_string.encode("utf-8")
        self.assertEqual(errorMessageElement.text.encode("utf-8"), encoded_string)

    def test_TC09_user_NOT_ChangePassword_in_Profile(self):
        #nav my.uda.edu.vn/home
        loginSuccess(self)

        #Profile my.uda.edu.vn/sv/thongtinsv
        profile(self)

        #CHECK CURRENT PASSWORD -> PASSWORD ĐÚNG
        changePassword(self, 'MainContent_Tptd', '0862567721')

        #TEST ĐỔI PASSWORD -> có Trim
        inputChangePassword(self, '3000212383', '')

        #Check the error message 'Password chưa đúng, vui lòng liên hệ trung tâm ICT' appear
        errorMessageElement = self.driver.find_element(By.ID,'MainContent_Ltbc')
        self.driver.save_screenshot('Step 13.png')
        my_string = "Kiểm tra lại yêu cầu password"
        encoded_string = my_string.encode("utf-8")
        self.assertEqual(errorMessageElement.text.encode("utf-8"), encoded_string)

    def test_TC010_user_NOT_ChangePassword_in_Profile(self):
        #nav my.uda.edu.vn/home
        loginSuccess(self)

        #Profile my.uda.edu.vn/sv/thongtinsv
        profile(self)

        #CHECK CURRENT PASSWORD -> PASSWORD ĐÚNG
        #find input changePassword worng pass
        ElementChangePassword = self.driver.find_element(By.ID, 'MainContent_Tptd')
        ElementChangePassword.send_keys('0862567721')

        #find button changpassword
        btnChangePassword = self.driver.find_element(By.ID, 'MainContent_Lrefesh')
        btnChangePassword.click()

        #TEST ĐỔI PASSWORD -> input > 3 key
        #find input Element changePassword
        ElementInputChangePassword = self.driver.find_element(By.ID, 'MainContent_Tpass')
        ElementInputChangePassword.send_keys('300')

        ElementAgainInputPassword = self.driver.find_element(By.ID, 'MainContent_Tnlp')
        ElementAgainInputPassword.send_keys('300')

        #Btn ChangePassword
        BtnChangePassword = self.driver.find_element(By.ID, 'MainContent_Ldo')
        BtnChangePassword.click()

        #Check the error message 'Password chưa đúng, vui lòng liên hệ trung tâm ICT' appear
        errorMessageElement = self.driver.find_element(By.ID,'MainContent_Ltbc')
        self.driver.save_screenshot('Step 14.png')
        my_string = "Kiểm tra lại yêu cầu password"
        encoded_string = my_string.encode("utf-8")
        self.assertEqual(errorMessageElement.text.encode("utf-8"), encoded_string)

if __name__ == '__main__':
    unittest.main()
