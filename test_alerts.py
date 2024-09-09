from pages.AlertsPage import AlertsPage

def test_alert(driver):
    
    """Verifies that the alert button was clicked, the JS alert closed 
    and that the HTML was modified accordingly.
    """
    
    # given
    page = AlertsPage(driver)   
    
    # when
    page.load()
    count_before = page.get_alert_count()
    page.click_alert_btn()
    alert = page.get_alert_text()
    page.accept_alert()
    count_after = page.get_alert_count()  # You need to first accept the alert before accessing the HTML again.
    alert_expl_text = page.get_alert_expl_text()
    
    # then
    assert count_after > count_before
    assert alert == 'I am an alert box!'
    assert alert_expl_text == 'You triggered and handled the alert dialog'
    
def test_confirm_accept(driver):
    
    """Verifies that the button was clicked, the JS confirm alert accepted
    and that the HTML was modified accordingly.
    """
    
    # given
    page = AlertsPage(driver)   
    
    # when
    page.load()
    count_before = page.get_confirm_count()
    page.click_confirm_btn()
    confirm = page.get_alert_text()
    page.accept_alert()
    count_after = page.get_confirm_count()
    confirm_expl_text = page.get_confirm_expl_text()
    confirm_return_text = page.get_confirm_return()
    
    # then
    assert count_after > count_before
    assert confirm == 'I am a confirm alert'
    assert confirm_expl_text == 'You clicked OK, confirm returned true.'
    assert confirm_return_text == 'true'

def test_confirm_dismiss(driver):
    
    """Verifies that the button was clicked, the JS confirm alert dismissed
    and that the HTML was modified accordingly.
    """
    
    # given
    page = AlertsPage(driver)
    
    # when
    page.load()
    count_before = page.get_confirm_count()
    page.click_confirm_btn()
    confirm = page.get_alert_text()
    page.dismiss_alert()
    count_after = page.get_confirm_count()
    confirm_expl_text = page.get_confirm_expl_text()
    confirm_return_text = page.get_confirm_return()
    
    # then
    assert count_after > count_before
    assert confirm == 'I am a confirm alert'
    assert confirm_expl_text == 'You clicked Cancel, confirm returned false.'
    assert confirm_return_text == 'false'

def test_prompt_accept(driver):
    
    """Verifies that the button was clicked, a string passed to the JS prompt,
    the prompt then accepted and HTML modified accordingly.
    """
    
    # given
    page = AlertsPage(driver)
    prompt_text = 'example'
    
    # when
    page.load()
    count_before = page.get_prompt_count()
    page.click_prompt_btn()
    confirm = page.get_alert_text()
    page.write_prompt(text=prompt_text)
    page.accept_alert()
    count_after = page.get_prompt_count()
    prompt_expl_text = page.get_prompt_expl_text()
    prompt_return_text = page.get_prompt_return()
    
    # then
    assert count_after > count_before
    assert confirm == 'I prompt you'
    assert prompt_expl_text == f"You clicked OK. 'prompt' returned {prompt_text}"
    assert prompt_return_text == prompt_text
    
def test_prompt_dismiss(driver):
    
    """Verifies that the button was clicked, the prompt then dismissed and HTML modified accordingly."""
    
    # given
    page = AlertsPage(driver)
    
    # when
    page.load()
    count_before = page.get_prompt_count()
    page.click_prompt_btn()
    confirm = page.get_alert_text()
    page.dismiss_alert()
    count_after = page.get_prompt_count()
    prompt_expl_text = page.get_prompt_expl_text()
        
    # then
    assert count_after > count_before
    assert confirm == 'I prompt you'
    assert prompt_expl_text == "You clicked Cancel. 'prompt' returned null"