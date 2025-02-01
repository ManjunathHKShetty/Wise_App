from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    button_mobile_XPath = "//button[contains(@class,'text--16 height-48 primary--text v-btn v-btn--block v-btn--has-bg theme--light v-size--default large secondary-bg')]"
    textbox_phoneNumber_XPath = "//input[@placeholder='Phone number']"
    button_getOTP_XPath = "//button[contains(@class,'mt-5')]"
    textbox_input1_XPath = "otp-field-box--0"
    textbox_input2_XPath = "otp-field-box--1"
    textbox_input3_XPath = "otp-field-box--2"
    textbox_input4_XPath = "otp-field-box--3"
    button_verify_XPath = "//button[@class='mt-6 v-btn v-btn--block v-btn--has-bg theme--light v-size--default large primary-bg ']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    def ClickContinueWithMobile(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_mobile_XPath))).click()

    def EnterPhoneNumber(self, phonenumber):
        phone_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.textbox_phoneNumber_XPath)))
        phone_input.clear()
        phone_input.send_keys(phonenumber)

    def ClickGetOtp(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_getOTP_XPath))).click()

    def EnterOtp(self, otp="0000"):
        otp_fields = [
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, self.textbox_input1_XPath))),
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, self.textbox_input2_XPath))),
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, self.textbox_input3_XPath))),
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, self.textbox_input4_XPath)))
        ]

        if len(otp) != len(otp_fields):
            raise ValueError(f"OTP length ({len(otp)}) does not match the number of OTP fields ({len(otp_fields)})")

        for i, digit in enumerate(otp):
            otp_fields[i].send_keys(digit)

    def ClickVerify(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_verify_XPath))).click()
