import pytest
from playwright.sync_api import expect

test_data = [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("problem_user", "secret_sauce", True),
    ("performance_glitch_user", "secret_sauce", True),
    ("error_user", "secret_sauce", True),
    ("visual_user", "secret_sauce", True),
]

@pytest.mark.parametrize("user, password, result", test_data)
def test_write_you_name_text(open_base_page, user, password, result):
    page = open_base_page
    select_user_name_element = page.locator('[id="user-name"]')
    select_user_name_element.fill(user)
    page.wait_for_timeout(1000)
    select_user_pass_element = page.locator('[id="password"]')
    select_user_pass_element.fill(password)
    button = page.get_by_role('button', name='Login')
    button.click()
    if result:
        page.wait_for_url('https://www.saucedemo.com/inventory.html')
    else:
        expect(page.locator('button.error-button')).to_be_visible()


