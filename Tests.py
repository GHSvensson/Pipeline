from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()

options.add_argument("--headless")
driver = webdriver.Chrome(options=options)


class TestFullscreentest:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_fullscreentest(self):
        self.driver.get("https://ghsvensson.github.io/NeonTyper/")
        self.driver.find_element(By.ID, "full-screen-button").click()
        elements = self.driver.find_elements(By.ID, "full-screen-button")
        assert len(elements) > 0
        self.driver.find_element(By.ID, "full-screen-button").click()


class TestGamefunctionalitytest:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_gamefunctionalitytest(self):
        self.driver.get("https://ghsvensson.github.io/NeonTyper/")
        elements = self.driver.find_elements(By.ID, "start-button")
        assert len(elements) > 0
        self.driver.find_element(By.CSS_SELECTOR, ".active").click()
        self.driver.find_element(By.ID, "start-button").click()
        self.driver.execute_script("window.scrollTo(0,75.55555725097656)")
        assert self.driver.find_element(By.CSS_SELECTOR, "h2").text == "You lost"
        self.driver.close()


class TestInstructionstest:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_instructionstest(self):
        self.driver.get("https://ghsvensson.github.io/NeonTyper/")
        self.driver.find_element(By.ID, "instr-button").click()
        elements = self.driver.find_elements(By.ID, "instr")
        assert len(elements) > 0
        self.driver.find_element(By.ID, "checkmark-button").click()
        self.driver.close()


class TestCorrecttitletest:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_correcttitletest(self):
        self.driver.get("https://ghsvensson.github.io/NeonTyper/")
        assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "NeonTyper"
