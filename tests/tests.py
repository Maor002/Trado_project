import pytest
from main.driver import create_driver
from main.funcs import get_login

base_url = 'http://test-admin-env.eba-fnn924ys.eu-west-1.elasticbeanstalk.com/#/login'


def test_language():
    actions = create_driver(base_url)
    assert get_login(actions).get("EN") == 'Phone*'
    assert get_login(actions).get("IL") == 'טלפון*'
    actions.close_driver()

