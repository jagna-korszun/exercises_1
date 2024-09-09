import pytest
import selenium.webdriver
import json

@pytest.fixture
def config(scope='session'):
    
    with open('config.json') as config_json:
        config = json.load(config_json)
    
    assert config['driver'] in ['Chrome', 'Firefox', 'Edge']
    
    return config
    
@pytest.fixture
def driver(config):
    
    if config['driver'] == 'Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument("--disable-search-engine-choice-screen")
        opts.add_argument('--disable-blink-features=AutomationControlled')
        d = selenium.webdriver.Chrome(options=opts)
    elif config['driver'] == 'Firefox':
        d = selenium.webdriver.Firefox()
    elif config['driver'] == 'Edge':
        d = selenium.webdriver.Edge()
    else:
        raise Exception('This browser is not supported')
    
    yield d
    d.quit()