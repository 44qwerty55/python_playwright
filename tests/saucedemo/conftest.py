import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage


@pytest.fixture
def open_base_page(page: Page):
    page.set_viewport_size({"width": 1600, "height": 1200})
    page.goto('https://www.saucedemo.com/')
    return page

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)


