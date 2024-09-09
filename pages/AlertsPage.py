from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AlertsPage:
    
    def __init__(self, driver):
        self.driver = driver
    
    url = 'https://testpages.eviltester.com/styled/alerts/alert-test.html'
    
    # locators
    explanation = (By.CLASS_NAME, 'explanation')
    alert_button = (By.ID, 'alertexamples')
    confirm_button = (By.ID, 'confirmexample')
    prompt_button = (By.ID, 'promptexample')
    alert_explanation = (By.ID, 'alertexplanation')
    confirm_explanation = (By.ID, 'confirmexplanation')
    prompt_explanation = (By.ID, 'promptexplanation')
    alert_return = (By.ID, 'alertreturn')
    confirm_return = (By.ID, 'confirmreturn')
    prompt_return = (By.ID, 'promptreturn')
    
    # selectors
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
    def get_confirm_expl_text(self):
        return self.driver.find_element(*self.confirm_explanation).text
    def get_prompt_expl_text(self):
        return self.driver.find_element(*self.prompt_explanation).text
    def get_alert_return(self):
        return self.driver.find_element(*self.alert_return).text
    def get_confirm_return(self):
        return self.driver.find_element(*self.confirm_return).text
    def get_prompt_return(self):
        return self.driver.find_element(*self.prompt_return).text
    def get_alert_count(self):
        return self.driver.find_element(*self.alert_return).get_attribute('data-use-count')
    def get_confirm_count(self):
        return self.driver.find_element(*self.confirm_return).get_attribute('data-use-count')
    def get_prompt_count(self):
        return self.driver.find_element(*self.prompt_return).get_attribute('data-use-count')
    
    # actions
    def load(self):
        self.driver.get(self.url)
    def click_alert_btn(self):
        button = self.get_alert_button()
        WebDriverWait(self.driver,200).until(EC.element_to_be_clickable(button)).click()
    def click_confirm_btn(self):
        button = self.get_confirm_button()
        WebDriverWait(self.driver,200).until(EC.element_to_be_clickable(button)).click()
    def click_prompt_btn(self):
        button = self.get_prompt_button()
        WebDriverWait(self.driver,200).until(EC.element_to_be_clickable(button)).click()
    def get_alert_text(self):  # I think this counts as an action and not selector but I am not sure.
        wait = WebDriverWait(self.driver, 2)
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        return alert_text
    def accept_alert(self):
        wait = WebDriverWait(self.driver, 2)
        alert = wait.until(EC.alert_is_present())  # It seems redundant to check for the alert being present twice. Is this approach correct?
        alert.accept()
    def dismiss_alert(self):
        wait = WebDriverWait(self.driver, 2)
        alert = wait.until(EC.alert_is_present())
        alert.dismiss()
    def write_prompt(self, text:str):
        wait = WebDriverWait(self.driver, 2)
        prompt = wait.until(EC.alert_is_present())
        prompt.send_keys(text)
        
    
    