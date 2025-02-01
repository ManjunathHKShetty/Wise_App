from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.customLogger import LogGen

class TimeLine:
    timeline_Xpath = "//a[normalize-space()='Timeline']"
    sessionCard_XPath = "//div[@class='d-flex align-center justify-space-between']"
    instructorName_XPath = "(//div[@class='v-avatar primary']/parent::span)[2]"
    sessionName_XPath = "(//div[@class='d-flex align-center justify-space-between']//div)[3]"
    sessionTime_XPath = "(//div[@class='d-flex align-center justify-space-between']//div)[6]"
    upcomingStatus_XPath = "//button[@value='FUTURE']/span/span"

    logger = LogGen.loggen()

    def __init__(self, driver, logger):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    def ClickOnTimeLine(self):
        try:
            self.logger.info("Clicking on the Timeline")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.timeline_Xpath))).click()
            self.logger.info("Successfully clicked on the Timeline.")
        except TimeoutException:
            self.logger.error("Failed to click on the Timeline element. Timeout occurred.")
            raise
        except ElementClickInterceptedException:
            self.logger.warning("Element was intercepted. Trying again...")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.timeline_Xpath))).click()

    def AssertSessionCard(self):
        try:
            self.logger.info("Waiting for the session card to be present.")
            return self.wait.until(EC.presence_of_element_located((By.XPATH, self.sessionCard_XPath)))
        except TimeoutException:
            self.logger.error("Session card not found within the given time.")
            raise

    def AssertInstructorName(self):
        try:
            self.logger.info("Fetching the instructor name.")
            return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.instructorName_XPath))).text.strip()
        except TimeoutException:
            self.logger.error("Instructor name not found.")
            raise

    def AssertSessionName(self):
        try:
            self.logger.info("Fetching the session name.")
            return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.sessionName_XPath))).text.strip()
        except TimeoutException:
            self.logger.error("Session name not found.")
            raise

    def AssertSessionTime(self):
        try:
            self.logger.info("Fetching the session time.")
            return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.sessionTime_XPath))).text.strip()
        except TimeoutException:
            self.logger.error("Session time not found.")
            raise

    def AssertUpcomingStatus(self):
        try:
            self.logger.info("Fetching the upcoming status.")
            return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.upcomingStatus_XPath))).text.strip()
        except TimeoutException:
            self.logger.error("Upcoming status not found.")
            raise