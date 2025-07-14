# import unittest
# import os
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import warnings

# username = os.getenv("abhilashks")  # Replace the username
# access_key = os.getenv("LT_vlepjdZXziyFBp5oW8m3LVYFQ5vpmplNFnDM8j5CpzkAmLw")  # Replace the access key


# capability = {
# 	"browserName": "Chrome",
# 	"browserVersion": "latest",
# 	"LT:Options": {
#         "username": username,
# 		"accessKey": access_key,
# 		"platformName": "linux",
#         "build": "Selenium 3 Example",
#         "name" : "Selenium 3 Sample Test",
#         "video": "True",
#         "console": "True",
#         "network": "True"
# 	}
# }

# def suppress_resource_warnings():
#     warnings.filterwarnings("ignore", category=ResourceWarning)

# class FirstSampleTest(unittest.TestCase):
#     driver = None

#     def setUp(self):
#         suppress_resource_warnings()
#         self.driver = webdriver.Remote(
#             command_executor = "http://{}:{}@hub.lambdatest.com/wd/hub".format(
#                 username, access_key
#             ),
#             # options=options,
#             desired_capabilities = capability
#         )

#     # """ You can write the test cases here """
#     def test_demo_site(self):
#         suppress_resource_warnings()
#         driver = self.driver
#         driver.implicitly_wait(10)
#         driver.set_page_load_timeout(30)
#         # driver.set_window_size(1920, 1080)

#         # Url
#         print("Loading URL")
#         driver.get(
#             "https://lambdatest.github.io/sample-todo-app/"
#         )

#         # Let's click on a element
#         driver.find_element(By.NAME, "li1").click()
#         location = driver.find_element(By.NAME, "li2")
#         location.click()
#         print("Clicked on the second element")

#         # Let's add a checkbox
#         driver.find_element(By.ID, "sampletodotext").send_keys("LambdaTest")
#         add_button = driver.find_element(By.ID, "addbutton")
#         add_button.click()
#         print("Added LambdaTest checkbox")

#         # print the heading
#         search = driver.find_element(By.CSS_SELECTOR, ".container h2")
#         assert search.is_displayed(), "heading is not displayed"
#         print(search.text)
#         search.click()
#         driver.implicitly_wait(3)

#          # Let's download the invoice
#         heading = driver.find_element(By.CSS_SELECTOR, ".container h2")
#         if heading.is_displayed():
#             heading.click()
#             driver.execute_script("lambda-status=passed")
#             print("Tests are run successfully!")
#         else:
#             driver.execute_script("lambda-status=failed")

#   # tearDown runs after each test case
#     def tearDown(self):
#         self.driver.quit()
       

# if __name__ == "__main__":
#     unittest.main()


# import unittest
# import os
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import warnings

# # Suppress resource warnings
# def suppress_resource_warnings():
#     warnings.filterwarnings("ignore", category=ResourceWarning)

# # Replace with your actual environment variable names
# username = os.getenv("LT_USERNAME", "abhilashks")
# access_key = os.getenv("LT_ACCESS_KEY", "LT_vlepjdZXziyFBp5oW8m3LVYFQ5vpmplNFnDM8j5CpzkAmLw")

# capability = {
#     "browserName": "Chrome",
#     "browserVersion": "latest",
#     "LT:Options": {
#         "username": username,
#         "accessKey": access_key,
#         "platformName": "Linux",  # Capital "L" is preferred
#         "build": "Selenium 3 Example",
#         "name": "Selenium 3 Sample Test",
#         "video": True,
#         "console": True,
#         "network": True
#     }
# }

# class FirstSampleTest(unittest.TestCase):
#     driver = None

#     def setUp(self):
#         suppress_resource_warnings()
#         self.driver = webdriver.Remote(
#             command_executor=f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub",
#             desired_capabilities=capability
#         )

#     def test_demo_site(self):
#         driver = self.driver
#         driver.implicitly_wait(10)
#         driver.set_page_load_timeout(30)

#         print("Loading URL")
#         driver.get("https://lambdatest.github.io/sample-todo-app/")

#         # Interactions
#         driver.find_element(By.NAME, "li1").click()
#         driver.find_element(By.NAME, "li2").click()
#         print("Clicked on the first and second checkboxes")

#         # Add task
#         driver.find_element(By.ID, "sampletodotext").send_keys("LambdaTest")
#         driver.find_element(By.ID, "addbutton").click()
#         print("Added LambdaTest checkbox")

#         # Validate heading
#         heading = driver.find_element(By.CSS_SELECTOR, ".container h2")
#         self.assertTrue(heading.is_displayed(), "Heading is not displayed")
#         print(f"Heading text: {heading.text}")
#         heading.click()

#         # Status marking
#         if heading.is_displayed():
#             driver.execute_script("lambda-status=passed")
#             print("Test Passed!")
#         else:
#             driver.execute_script("lambda-status=failed")

#     def tearDown(self):
#         if self.driver:
#             self.driver.quit()

# if __name__ == "__main__":
#     unittest.main()


import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# Fetch credentials from environment variables or fallback
username = os.getenv("LT_USERNAME", "abhilashks")
access_key = os.getenv("LT_ACCESS_KEY", "LT_vlepjdZXziyFBp5oW8m3LVYFQ5vpmplNFnDM8j5CpzkAmLw")

# LambdaTest capabilities
capabilities = {
    "browserName": "Chrome",
    "browserVersion": "latest",
    "LT:Options": {
        "username": username,
        "accessKey": access_key,
        "platformName": "Linux",
        "build": "Selenium 3 Example",
        "name": "Selenium 3 Sample Test",
        "video": True,
        "console": True,
        "network": True
    }
}

class FirstSampleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor=f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub",
            desired_capabilities=capabilities
        )

    def test_demo_site(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)

        # Open the sample app
        print("Opening Sample ToDo App")
        driver.get("https://lambdatest.github.io/sample-todo-app/")

        # Interact with checkboxes
        driver.find_element(By.NAME, "li1").click()
        driver.find_element(By.NAME, "li2").click()
        print("Checked two default items")

        # Add a new item
        driver.find_element(By.ID, "sampletodotext").send_keys("LambdaTest")
        driver.find_element(By.ID, "addbutton").click()
        print("Added new todo item: LambdaTest")

        # Check for heading visibility
        heading = driver.find_element(By.CSS_SELECTOR, ".container h2")
        self.assertTrue(heading.is_displayed(), "Heading is not displayed")
        print(f"Heading: {heading.text}")

        # Report test result to LambdaTest
        driver.execute_script("lambda-status=passed")

    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
