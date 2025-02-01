import pytest
from pageObjects.Schedule_Session import ScheduleSession
from pageObjects.Login_Page import LoginPage
from pageObjects.Homescreen_Page import HomeScreen
from Utilities.readProperties import ReadConfig
from pageObjects.Timeline_Page import TimeLine
from Utilities.customLogger import LogGen


@pytest.mark.usefixtures("setup")
class TestCase:
    baseURL = ReadConfig.getApplicationURL()
    phonenumber = ReadConfig.getPhoneNumber()
    logger = LogGen.loggen()

    def test_login(self):
        """Test login functionality"""
        self.driver.get(self.baseURL)
        self.logger.info(f"Opened URL: {self.baseURL}")

        self.lp = LoginPage(self.driver)
        self.logger.info("Clicking 'Continue with Mobile' button.")
        self.lp.ClickContinueWithMobile()

        self.logger.info(f"Entering phone number: {self.phonenumber}")
        self.lp.EnterPhoneNumber(self.phonenumber)

        self.logger.info("Clicking 'Get OTP' button.")
        self.lp.ClickGetOtp()

        otp = "0000"
        self.logger.info(f"Entering OTP: {otp}")
        self.lp.EnterOtp(otp)

        self.logger.info("Clicking 'Verify' button.")
        self.lp.ClickVerify()

    def test_home_screen(self):
        """Test home screen functionality"""
        self.hs = HomeScreen(self.driver)
        expected_text = "Testing Institute"
        actual_text = self.hs.HomeScreenText()
        self.logger.info(f"Home screen text: {actual_text}")
        assert actual_text == expected_text, f"Institution name does not match! Expected: {expected_text}, but got: {actual_text}"

        self.logger.info("Navigating to Classroom")
        self.hs.ClickGroupCourses()
        self.hs.ClickOnClassroomForAutomatedTesting()

        expected_classroom_text = "Classroom for Automated testing"
        actual_classroom_text = self.hs.VerifyClassroomForAutomatedTestingText()
        self.logger.info(f"Classroom text: {actual_classroom_text}")
        assert actual_classroom_text == expected_classroom_text, f"Expected '{expected_classroom_text}', but got '{actual_classroom_text}'"

    def test_schedule_session(self):
        """Test session scheduling"""
        self.logger.info("Scheduling a session")
        self.ss = ScheduleSession(self.driver, self.logger)

        self.logger.info("Clicking 'Live Sessions' tab.")
        self.ss.ClickLiveSessions()

        self.logger.info("Clicking 'Schedule Sessions' button.")
        self.ss.ClickScheduleSessions()

        self.logger.info("Clicking 'Add Session' button.")
        self.ss.ClickAddSession()

        self.logger.info("Selecting Time")
        self.ss.SelectTime()

        self.logger.info("Clicking 'Create' button to schedule the session.")
        self.ss.ClickCreate()

        self.logger.info("Clicking 'Back' button")
        self.ss.ClickBack()

        self.logger.info("Session scheduled successfully.")

    def test_timeline_session_details(self):
        """Test timeline session details"""
        self.logger.info("Initializing Timeline Page Object")
        tl = TimeLine(self.driver, self.logger)

        self.logger.info("Clicking on Timeline")
        tl.ClickOnTimeLine()

        self.logger.info("Verifying if Session Card is displayed on the Timeline")
        assert tl.AssertSessionCard().is_displayed(), "Session card is not displayed on the timeline"

        instructor_name = tl.AssertInstructorName()
        self.logger.info(f"Verifying Instructor Name: Expected 'Wise Tester', Found '{instructor_name}'")
        assert instructor_name == "Wise Tester", f"Unexpected instructor name: {instructor_name}"

        session_name = tl.AssertSessionName()
        self.logger.info(f"Verifying Session Name: Expected to contain 'Live session', Found '{session_name}'")
        assert "Live session" in session_name, f"Unexpected session name: {session_name}"

        session_time = tl.AssertSessionTime()
        self.logger.info(f"Verifying Session Time: Expected '10:00 PM', Found '{session_time}'")
        assert session_time == "10:00 PM", f"Unexpected session time: {session_time}"

        upcoming_status = tl.AssertUpcomingStatus().strip("()")
        self.logger.info(f"Verifying Upcoming Status: Found '{upcoming_status}'")

        assert upcoming_status.isdigit() and int(upcoming_status) > 0, \
            f"Unexpected upcoming status: {upcoming_status}. Expected a number greater than 0."

