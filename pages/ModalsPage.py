from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ModalsPage:
    
    def __init__(self, driver):
        self.driver = driver
        
    url = 'https://testpages.eviltester.com/styled/alerts/fake-alert-test.html'
        
    # locators
    explanation = (By.CLASS_NAME, 'explanation')
    alert_button = (By.ID, 'fakealert')
    dialog_button = (By.ID, 'modaldialog')
    dialog = (By.XPATH, "//div[@role='dialog']")
    dialog_text = (By.ID, 'dialog-text')
    ok_button = (By.ID, 'dialog-ok')
    page_body = (By.CLASS_NAME, 'page-body')
    
    # selectors
    def get_url(self):
        return self.driver.current_url
    def get_explanation(self):
        return self.driver.find_element(*self.explanation)
    def explanation_displayed(self):
        return self.get_explanation().is_displayed()
    def get_alert_button(self):
        return self.driver.find_element(*self.alert_button)
    def get_dialog_button(self):
        return self.driver.find_element(*self.dialog_button)
    def get_alert_count(self):
        return self.driver.find_element(*self.alert_button).get_attribute('data-click-count')
    def get_dialog_count(self):
        return self.driver.find_element(*self.dialog_button).get_attribute('data-click-count')
    def get_dialog(self):
        return self.driver.find_element(*self.dialog)
    def get_dialog_class(self):
        return self.driver.find_element(*self.dialog).get_attribute('class')
    def get_ok_button(self):
        return self.driver.find_element(*self.ok_button)
    def get_dialog_text(self):
        return self.driver.find_element(*self.dialog_text).text
    def get_page_body(self):
        return self.driver.find_element(*self.page_body)
    
    # actions
    def load(self):
        self.driver.get(self.url)
    def click_alert_btn(self):
        button = self.get_alert_button()
        WebDriverWait(self.driver,2).until(EC.element_to_be_clickable(button)).click()
    def click_dialog_btn(self):
        button = self.get_dialog_button()
        WebDriverWait(self.driver,2).until(EC.element_to_be_clickable(button)).click()
    def click_ok(self):
        ok = self.get_ok_button()
        ok.click()
    def click_background(self):
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(self.dialog))) # This lets us avoid the ElementClickInterceptedException.