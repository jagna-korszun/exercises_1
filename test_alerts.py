from pages.AlertsPage import AlertsPage

def test_alert(driver):
    
    #given
    page = AlertsPage(driver)   
    
    #when
    page.load()
    page.click_alert_btn()
    alert = page.get_alert_text()
    page.accept_alert()
    alert_expl_text = page.get_alert_expl_text()
        
    #then
    assert alert == 'I am an alert box!'
    assert alert_expl_text == 'You triggered and handled the alert dialog'
    
    
