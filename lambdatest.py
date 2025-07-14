# 

# import unittest
# import os
# import json
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.common.exceptions import WebDriverException

# # Ensure reports directory exists
# os.makedirs("reports", exist_ok=True)

# # Get credentials from environment variables or use fallback values
# username = os.getenv("LT_USERNAME", "abhilashks")
# access_key = os.getenv("LT_ACCESS_KEY", "LT_vlepjdZXziyFBp5oW8m3LVYFQ5vpmplNFnDM8j5CpzkAmLw")

# # Chrome options and LambdaTest capabilities
# options = ChromeOptions()
# options.browser_version = "latest"
# options.platform_name = "Windows 10"

# lt_options = {
#     "username": username,
#     "accessKey": access_key,
#     "video": True,
#     "network": True,
#     "console": True,
#     "resolution": "1920x1080",
#     "build": "Selenium 3 Example",
#     "name": "Selenium 3 Sample Test",
#     "w3c": True,
#     "plugin": "python-python"
# }

# options.set_capability("LT:Options", lt_options)

# class FirstSampleTest(unittest.TestCase):
#     driver = None

#     def setUp(self):
#         try:
#             self.driver = webdriver.Remote(
#                 command_executor=f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub",
#                 options=options
#             )
#             print("Connected to LambdaTest hub.")
#         except WebDriverException as e:
#             self.fail(f"Failed to connect to LambdaTest hub: {e}")

#     def test_demo_site(self):
#         driver = self.driver
#         driver.implicitly_wait(10)
#         driver.set_page_load_timeout(30)
#         driver.set_window_size(1920, 1080)

#         print("Loading demo URL")
#         driver.get("https://stage-lambda-devops-use-only.lambdatestinternal.com/To-do-app/index.html")
        
#         # Click tasks
#         driver.find_element(By.NAME, "li1").click()
#         driver.find_element(By.NAME, "li2").click()
#         print("Clicked on the first and second checkboxes")

#         # Smart UI screenshot
#         # try:
#         #     driver.execute_script("smartui.takeScreenshot")
#         #     print("Smart UI screenshot taken")
#         # except Exception as e:
#         #     print(f"Smart UI screenshot skipped or failed: {e}")

#         # Add new task
#         driver.find_element(By.ID, "sampletodotext").send_keys("LambdaTest")
#         driver.find_element(By.ID, "addbutton").click()
#         print("Added 'LambdaTest' task")

#         # Verify heading
#         heading = driver.find_element(By.CSS_SELECTOR, ".container h2")
#         self.assertTrue(heading.is_displayed(), "Heading is not displayed")
#         print(f"Heading found: {heading.text}")

#         heading.click()
#         time.sleep(3)

#         # Mark test as passed/failed
#         if heading.is_displayed():
#             driver.execute_script("lambda-status=passed")
#             print("Test passed")
#         else:
#             driver.execute_script("lambda-status=failed")
#             print("Test failed")

#     def tearDown(self):
#         if self.driver:
#             self.driver.quit()

# # Custom test result class to write a JSON report
# class JSONTestResult(unittest.TestResult):
#     def __init__(self):
#         super().__init__()
#         self.results = []

#     def addSuccess(self, test):
#         super().addSuccess(test)
#         self.results.append({"test": str(test), "status": "passed", "error": None})

#     def addFailure(self, test, err):
#         super().addFailure(test, err)
#         self.results.append({"test": str(test), "status": "failed", "error": self._exc_info_to_string(err, test)})

#     def addError(self, test, err):
#         super().addError(test, err)
#         self.results.append({"test": str(test), "status": "error", "error": self._exc_info_to_string(err, test)})

#     def save_json(self):
#         report = {
#             "timestamp": time.ctime(),
#             "tests": self.results,
#             "passed": self.testsRun - len(self.failures) - len(self.errors),
#             "failed": len(self.failures),
#             "errors": len(self.errors)
#         }
#         with open("reports/test_report.json", "w") as f:
#             json.dump(report, f, indent=4)

# def run_tests():
#     suite = unittest.TestLoader().loadTestsFromTestCase(FirstSampleTest)
#     result = JSONTestResult()
#     suite.run(result)
#     result.save_json()
#     return result

# if __name__ == "__main__":
#     result = run_tests()
#     if result.wasSuccessful():
#         print("All tests passed!")
#     else:
#         print("Some tests failed or had errors.")


import unittest
import os
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import WebDriverException

# Ensure reports directory exists
os.makedirs("reports", exist_ok=True)

# Get credentials from environment variables or use fallback values
username = os.getenv("LT_USERNAME", "abhilashks")
access_key = os.getenv("LT_ACCESS_KEY", "LT_vlepjdZXziyFBp5oW8m3LVYFQ5vpmplNFnDM8j5CpzkAmLw")

# Chrome options and LambdaTest capabilities
options = ChromeOptions()
options.browser_version = "latest"
options.platform_name = "Windows 10"

lt_options = {
    "username": username,
    "accessKey": access_key,
    "video": True,
    "network": True,
    "console": True,
    "resolution": "1920x1080",
    "build": "Selenium 3 new Example",
    "name": "Selenium 3 new Sample Test",
    "w3c": True,
    "plugin": "python-python"
}

options.set_capability("LT:Options", lt_options)

class FirstSampleTest(unittest.TestCase):
    driver = None

    def setUp(self):
        try:
            self.driver = webdriver.Remote(
                command_executor=f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub",
                options=options
            )
            print("Connected to LambdaTest hub.")
        except WebDriverException as e:
            self.fail(f"Failed to connect to LambdaTest hub: {e}")

    def test_demo_site(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

        print("Loading demo URL")
        driver.get("https://stage-lambda-devops-use-only.lambdatestinternal.com/To-do-app/index.html")
        time.sleep(2)

        # Click tasks
        driver.find_element(By.NAME, "li1").click()
        time.sleep(2)
        driver.find_element(By.NAME, "li2").click()
        print("Clicked on the first and second checkboxes")
        time.sleep(2)

        # Add new task
        driver.find_element(By.ID, "sampletodotext").send_keys("LambdaTest")
        time.sleep(2)
        driver.find_element(By.ID, "addbutton").click()
        print("Added 'LambdaTest' task")
        time.sleep(2)

        # Verify heading
        heading = driver.find_element(By.CSS_SELECTOR, ".container h2")
        self.assertTrue(heading.is_displayed(), "Heading is not displayed")
        print(f"Heading found: {heading.text}")
        time.sleep(2)

        heading.click()
        time.sleep(3)

        # Mark test as passed/failed
        if heading.is_displayed():
            driver.execute_script("lambda-status=passed")
            print("Test passed")
        else:
            driver.execute_script("lambda-status=failed")
            print("Test failed")

    def tearDown(self):
        if self.driver:
            self.driver.quit()

# Custom test result class to write a JSON report
class JSONTestResult(unittest.TestResult):
    def __init__(self):
        super().__init__()
        self.results = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.results.append({"test": str(test), "status": "passed", "error": None})

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.results.append({"test": str(test), "status": "failed", "error": self._exc_info_to_string(err, test)})

    def addError(self, test, err):
        super().addError(test, err)
        self.results.append({"test": str(test), "status": "error", "error": self._exc_info_to_string(err, test)})

    def save_json(self):
        report = {
            "timestamp": time.ctime(),
            "tests": self.results,
            "passed": self.testsRun - len(self.failures) - len(self.errors),
            "failed": len(self.failures),
            "errors": len(self.errors)
        }
        with open("reports/test_report.json", "w") as f:
            json.dump(report, f, indent=4)

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstSampleTest)
    result = JSONTestResult()
    suite.run(result)
    result.save_json()
    return result

if __name__ == "__main__":
    result = run_tests()
    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print("Some tests failed or had errors.")
