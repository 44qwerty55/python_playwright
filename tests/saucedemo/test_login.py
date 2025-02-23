import pytest
from playwright.sync_api import expect, Page

from data.default_snapshots import INVENTORY_DEFAULT_SNAPSHOT
from data.default_users import DefaultUsers
from data.urls_data import INVENTORY_PAGE_URL
from model.user import User

default_users = DefaultUsers()
test_data = [
    (default_users.get_standard_user(), INVENTORY_DEFAULT_SNAPSHOT),
    (default_users.get_visual_user(),  INVENTORY_DEFAULT_SNAPSHOT),
    (default_users.get_performance_glitch_user(), INVENTORY_DEFAULT_SNAPSHOT),
    (default_users.get_error_user(), INVENTORY_DEFAULT_SNAPSHOT),
    (default_users.get_problem_user(), INVENTORY_DEFAULT_SNAPSHOT),
]

@pytest.mark.parametrize("user, snapshot_page", test_data)
def test_login(login_page, inventory_page, open_base_page, user: User, snapshot_page: str):
    page = open_base_page
    login_page.login_to_system(user.get_name(), user.get_password())

    expect(page).to_have_url(INVENTORY_PAGE_URL)
    inventory_page.validate_title("Products")
    inventory_page.validate_snapshot(snapshot_page)



