import pytest
from playwright.sync_api import Page

from data.urls_data import TEST_CAFE_PAGE


@pytest.fixture
def open_base_page(page: Page):
    page.set_viewport_size({"width": 1600, "height": 1200})
    page.goto(TEST_CAFE_PAGE)
    return page

