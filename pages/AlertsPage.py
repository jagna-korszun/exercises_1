from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AlertsPage:
    
    def __init__(self, driver):
        self.driver = driver
        
    url = 'https://testpages.eviltester.com/styled/alerts/alert-test.html'
        
    #locators
    explanation = (By.CLASS_NAME, 'explanation')
    alert_button = (By.ID, 'alertexamples')
    confirm_button = (By.ID, 'confirmexamples')
    prompt_button = (By.ID, 'promptexamples')
    alert_explanation = (By.ID, 'alertexplanation')
    
    #selectors
    def get_url(self):
        return self.driver.current_url
    def get_explanation(self):
        return self.driver.find_element(*self.explanation)
    def explanation_displayed(self):
        return self.get_explanation().is_displayed()
    def get_alert_button(self):
        return self.driver.find_element(*self.alert_button)
    def get_confirm_button(self):
        return self.driver.find_element(*self.confirm_button)
    def get_prompt_button(self):
        return self.driver.find_element(*self.prompt_button)
    def get_alert_expl_text(self):
        return self.driver.find_element(*self.alert_explanation).text
    
    #actions
    def load(self):
        self.driver.get(self.url)
    def click_alert_btn(self):
        self.get_alert_button().click()
    def click_confirm_btn(self):
        self.get_confirm_button().click()
    def click_prompt_btn(self):
        self.get_prompt_button().click()
    def get_alert_text(self):
        wait = WebDriverWait(self.driver, 5)
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        return alert_text
    def accept_alert(self):
        wait = WebDriverWait(self.driver, 2)
        alert = wait.until(EC.alert_is_present()) # trochę koślawe, że dwa razy sprawdzam, czy jest alert
        alert.accept()
    