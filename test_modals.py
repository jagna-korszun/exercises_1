from pages.ModalsPage import ModalsPage

def test_modal_alert(driver):
    
    """Verifies that the button was clicked, the modal alert then closed and that the HTML was modified accordingly."""
    
    # given
    page = ModalsPage(driver)   

    # when
    page.load()
    count_before = page.get_alert_count()
    page.click_alert_btn()
    count_after = page.get_alert_count()
    dialog_class = page.get_dialog_class()
    dialog_text = page.get_dialog_text()
    page.click_ok()
    
    # then
    assert count_after > count_before
    assert dialog_class == 'dialog active'
    assert dialog_text == 'I am a fake alert box!'
    
def test_modal_dialog(driver):
    
    """Verifies that the button was clicked, the modal dialog then closed by clicking
    the background and that the HTML was modified accordingly.
    """
    
    # given
    page = ModalsPage(driver)   
    
    # when
    page.load()
    count_before = page.get_dialog_count()
    page.click_dialog_btn()
    count_after = page.get_dialog_count()
    dialog_class = page.get_dialog_class()
    dialog_text = page.get_dialog_text()
    page.click_background()
        
    # then
    assert count_after > count_before
    assert dialog_class == 'dialog active'
    assert dialog_text == 'I am a modal div!'
