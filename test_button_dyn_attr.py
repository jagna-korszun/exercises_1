from pages.AttributesPage import AttributesPage

def test_button_dyn_attr(driver):
    
    """Verifies that the button was clicked and HTML modified."""
    
    # given
    attributes_page = AttributesPage(driver)
    
    # when
    attributes_page.load()
    attr_before = attributes_page.get_current_id()
    attributes_page.click()
    attr_after = attributes_page.get_current_id()
    
    # then
    assert attr_after > attr_before