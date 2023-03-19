import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestFullscreentest:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_fullscreentest(self):
        self.driver.get("https://ghsvensson.github.io/NeonTyper/")
        self.driver.find_element(By.ID, "full-screen-button").click()
        self.driver.find_element(By.ID, "full-screen-button").click()
