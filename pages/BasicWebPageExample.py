from selenium.webdriver.common.by import By

class BasicWebPageExample:
    
    def __init__(self, browser):
        self.driver = browser
    
    url = "https://testpages.eviltester.com/styled/basic-web-page-test.html"
    explanation = (By.CLASS_NAME, 'explanation')
    
    def get_url(self):
        return self.driver.current_url
    def get_explanation(self):
        return self.driver.find_element(*self.explanation)
    def explanation_displayed(self):
        return self.get_explanation().is_displayed()
    
    def load(self):
        self.driver.get(self.url)
    