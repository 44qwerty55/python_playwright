import pytest
from playwright.sync_api import Page


@pytest.fixture
def open_base_page(page: Page):
    page.set_viewport_size({"width": 1600, "height": 1200})
    page.goto('https://www.saucedemo.com/')
    return page


