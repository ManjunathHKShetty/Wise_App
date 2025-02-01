from selenium.common import TimeoutException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.customLogger import LogGen

class ScheduleSession:
    live_sessions_XPath = "//a[normalize-space()='Live Sessions']"
    schedule_sessions_XPath1 = "//button[contains(@class,'mt-2 mt-sm-0 v-btn v-btn--has-bg theme--light v-size--default small primary-bg')]"
    schedule_sessions_XPath2 = "//button[contains(@class,'mr-2 v-btn v-btn--has-bg theme--light v-size--default small secondary-bg')]"
    add_session_XPath = "//button[contains(@class,'mb-3 px-2 v-btn v-btn--block v-btn--has-bg theme--light v-size--default small secondary-bg')]"
    time_picker_XPath = "(//div[@class='v-select__slot']//input[starts-with(@id, 'input-')])[4]"
    select_meridian_XPath = "//div[@class='text--16']"
    create_button_XPath = "//button[@class='v-btn v-btn--has-bg theme--light v-size--default medium primary-bg ']"
    back_button_XPath = "//button[@class='v-icon notranslate mr-2 v-icon--link mdi mdi-arrow-left theme--light']"

    logger = LogGen.loggen()

    def __init__(self, driver, logger):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    def ClickLiveSessions(self):
        try:
            self.logger.info("Clicking on 'Live Sessions'.")
            live_sessions_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.live_sessions_XPath)))
            live_sessions_button.click()
        except TimeoutException:
            self.logger.error("'Live Sessions' button not found. Timeout occurred.")
            raise

    def ClickScheduleSessions(self):
        self.logger.info("Clicking 'Schedule Sessions' button.")
        try:
            schedule_button1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.schedule_sessions_XPath1)))
            self.logger.info("Found 'Schedule Sessions' button (Primary). Clicking it.")
            schedule_button1.click()
        except TimeoutException:
            self.logger.warning("'Schedule Sessions' button (Primary) not found. Trying Secondary button.")
            try:
                schedule_button2 = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.schedule_sessions_XPath2)))
                self.logger.info("Found 'Schedule Sessions' button (Secondary). Clicking it.")
                schedule_button2.click()
            except TimeoutException:
                self.logger.error("Both 'Schedule Sessions' buttons were not found. Failing the test.")
                assert False, "Failed to find and click 'Schedule Sessions' button."

    def ClickAddSession(self):
        max_retries = 3  # Retry up to 3 times if stale element error occurs
        for attempt in range(max_retries):
            try:
                self.logger.info(f"Attempt {attempt + 1}: Clicking 'Add Session' button.")
                add_session_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.add_session_XPath)))
                add_session_button.click()
                return  # Exit the loop if click succeeds
            except StaleElementReferenceException:
                self.logger.warning("Element became stale. Retrying...")

        self.logger.error("Failed to click 'Add Session' button after multiple attempts.")
        assert False, "StaleElementReferenceException: Unable to click 'Add Session'."

    def SelectTime(self):
        try:
            # Locate and click the time picker input field
            time_picker = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, self.time_picker_XPath)))
            self.logger.info("Clicking time picker input field.")
            time_picker.click()

            # Clear the existing value (optional) and send the new time value
            self.logger.info("Clearing the existing time value and entering '10:00'.")
            time_picker.clear()  # Clear the field if necessary
            time_picker.send_keys("10:00")

            # Wait and click the AM/PM selector (if applicable)
            select_meridian = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.select_meridian_XPath))
            )
            self.logger.info("Selecting AM/PM as session meridian.")
            select_meridian.click()

        except TimeoutException:
            self.logger.error("Failed to select time. Timeout occurred.")
            raise

    def ClickCreate(self):
        try:
            self.logger.info("Clicking 'Create' button to schedule the session.")
            create_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.create_button_XPath)))
            create_button.click()
        except TimeoutException:
            self.logger.error("'Create' button not found. Timeout occurred.")
            raise

    def ClickBack(self):
        try:
            self.logger.info("Clicking 'Back' button.")
            back_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.back_button_XPath)))
            back_button.click()
        except TimeoutException:
            self.logger.error("'Back' button not found. Timeout occurred.")
            raise
