from pages.BasicWebPageExample import BasicWebPageExample
from pages.AttributesPage import AttributesPage
from pages.DynamicTablePage import DynamicTablePage
from pages.AlertsPage import AlertsPage
from pages.ModalsPage import ModalsPage
import pytest

@pytest.mark.parametrize('page_type',[BasicWebPageExample, AttributesPage, DynamicTablePage, AlertsPage, ModalsPage])
def test_run_explain(driver, page_type):
    
    """Verifies that both the URL of the loaded page is correct and that the explanation is displayed.
    Uses parametrization to load different pages in a sequence."""
    
    # given
    page = page_type(driver)
    
    # when
    page.load()
    new_url = page.get_url()
    explanation_displayed = page.explanation_displayed()
    
    # then
    assert new_url == page.url
    assert explanation_displayed
    
    
    
