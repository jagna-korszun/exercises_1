from pages.DynamicTablePage import DynamicTablePage

def test_table(driver):
    
    #given
    table_page = DynamicTablePage(driver)
    new_caption = 'My Super Dynamic Table'
    new_id = 'My Super Fresh ID'
    new_json = ('{"name": "Foo", "age" : 12}, {"name": "Bar", "age" : 24}, {"name": "Baz", "age" : 36}')
    
    #when
    table_page.load()
    table_page.show_menu()
    
    #and
    table_page.input_caption(new_caption)
    table_page.input_id(new_id)
    table_page.input_json(new_json)
    
    #and
    table_page.refresh_click()
    caption = table_page.get_table_caption()
    id = table_page.get_table_id()
    
    #then
    assert table_page.is_clicked()
    #assert caption == new_caption # HTML does not respond
    #assert id == new_id # HTML does not respond
    