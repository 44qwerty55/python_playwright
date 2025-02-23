import pytest
from playwright.sync_api import Page

from data.default_users import DefaultUsers
from data.urls_data import AUTHN_PAGE_URL
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_first_step_page import CheckoutFirstStepPage
from pages.checkout_second_step_page import CheckoutSecondStepPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.shopping_cart_page import ShoppingCartPage


@pytest.fixture
def open_base_page(page: Page):
    page.set_viewport_size({"width": 1600, "height": 1200})
    page.goto(AUTHN_PAGE_URL)
    return page

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page: Page):
    return InventoryPage(page)

@pytest.fixture
def shopping_cart_page(page: Page):
    return ShoppingCartPage(page)

@pytest.fixture
def checkout_first_step_page(page: Page):
    return CheckoutFirstStepPage(page)

@pytest.fixture
def checkout_second_step_page(page: Page):
    return CheckoutSecondStepPage(page)

@pytest.fixture
def checkout_complete_page(page: Page):
    return CheckoutCompletePage(page)

@pytest.fixture
def get_default_users():
    return DefaultUsers()
