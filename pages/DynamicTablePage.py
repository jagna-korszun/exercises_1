from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DynamicTablePage:
    
    def __init__(self, browser):
        self.driver = browser
    
    url = "https://testpages.eviltester.com/styled/tag/dynamic-table.html"
    
    # locators
    explanation = (By.CLASS_NAME, 'explanation')
    caption_input = (By.ID, 'caption')
    id_input = (By.ID, 'tableid')
    jsondata = (By.ID, 'jsondata')
    summary = (By.TAG_NAME, 'summary')
    button = (By.ID, 'refreshtable')
    table_caption = (By.TAG_NAME, 'caption')
    table_id = (By.TAG_NAME, 'table')
    
    # selectors
    def get_explanation(self):
        return self.driver.find_element(*self.explanation)
    def explanation_displayed(self):
        return self.get_explanation().is_displayed()
    def get_caption_input(self):
        return self.driver.find_element(*self.caption_input)
    def get_id_input(self):
        return self.driver.find_element(*self.id_input)
    def get_json_input(self):
        return self.driver.find_element(*self.jsondata)
    def get_button(self):
        return self.driver.find_element(*self.button)
    def get_table_caption(self):
        return self.driver.find_element(*self.table_caption)
    def get_menu(self):
        return self.driver.find_element(*self.summary)
    
    # actions
    def load(self):
        self.driver.get(self.url)
    def get_url(self):  # I think this counts as an action and not selector but I am not sure.
        return self.driver.current_url
    def input_caption(self, caption):
        caption_input = self.get_caption_input()
        caption_input.clear()
        caption_input.send_keys(caption + Keys.RETURN)
    def input_id(self, new_id):
        id_input = self.get_id_input()
        id_input.clear()
        id_input.send_keys(new_id + Keys.RETURN)
    def input_json(self, new_json):
        json = self.get_json_input()
        json.clear()
        json.send_keys(new_json + Keys.RETURN)
    def show_menu(self):
        summary = self.get_menu()
        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(summary)).click()
    def refresh_click(self):
        '''Since the button does not execute the JS script while the browser is being run through a driver,
        I used an event listener script to prove that the button is indeed clicked'''
        button = self.get_button()
        self.driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});", button)
        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(button)).click()
    def is_clicked(self):
        return self.get_button().get_attribute('automationTrack')
    def get_table_caption(self):
        time.sleep(2)
        return self.driver.find_element(*self.table_caption).text
    def get_table_id(self):
        time.sleep(2)
        return self.driver.find_element(*self.table_id).get_attribute('id')
    
    

    