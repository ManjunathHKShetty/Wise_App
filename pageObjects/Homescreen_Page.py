from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomeScreen:
    home_screen_display_Xpath = "//div[@class='name text--24 font-weight--600 ml-3']"
    group_courses_XPath = "//a[4]"
    classroom_for_automated_testing_XPath = "//a[normalize-space()='Classroom for Automated testing']"
    classroom_for_automated_testing_text_XPath = "//div[@class='text--24 font-weight--600']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def HomeScreenText(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.home_screen_display_Xpath))).text

    def ClickGroupCourses(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.group_courses_XPath))).click()

    def ClickOnClassroomForAutomatedTesting(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.classroom_for_automated_testing_XPath))).click()

    def VerifyClassroomForAutomatedTestingText(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.classroom_for_automated_testing_text_XPath))).text
