from pages.BasicWebPageExample import BasicWebPageExample
from pages.AttributesPage import AttributesPage
from pages.DynamicTablePage import DynamicTablePage
import pytest

@pytest.mark.parametrize('page_type',[BasicWebPageExample, AttributesPage, DynamicTablePage])
def test_run_explain(driver, page_type):
    
    #given
    page = page_type(driver)
    
    #when
    page.load()
    new_url = page.get_url()
    explanation_displayed = page.explanation_displayed()
    
    #then
    assert new_url == page.url
    assert explanation_displayed
    
    
    
