from selenium.webdriver.common.by import By

class AttributesPage:
    
    def __init__(self, driver):
        self.driver = driver
    
    url = "https://testpages.eviltester.com/styled/attributes-test.html"
    explanation = (By.CLASS_NAME, 'explanation')
    button = (By.CLASS_NAME, 'styled-click-button')
    p_dynamic = (By.ID, 'jsattributes')
    
    def get_url(self):
        return self.driver.current_url
    def get_explanation(self):
        return self.driver.find_element(*self.explanation)
    def explanation_displayed(self):
        return self.get_explanation().is_displayed()
    def get_dynamic(self):
        return self.driver.find_element(*self.p_dynamic)
    def get_current_id(self):
        return self.driver.get_dynamic().get_attribute('nextid')
    
    def load(self):
        self.driver.get(self.url)
    def click(self):
        self.driver.find_element(*self.button).click()
    
    