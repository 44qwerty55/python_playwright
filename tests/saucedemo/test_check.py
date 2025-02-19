import pytest
from playwright.sync_api import expect

test_data = [
    ("standard_user", "secret_sauce", True, None),
    ("locked_out_user", "secret_sauce", False, "Epic sadface: Sorry, this user has been locked out."),
    ("problem_user", "secret_sauce", True, None),
    ("performance_glitch_user", "secret_sauce", True, None),
    ("error_user", "secret_sauce", True, None),
    ("visual_user", "secret_sauce", True, None),
    ("visual_user", "another_value", False, "Epic sadface: Username and password do not match any user in this service"),
    ("visual_user", "", False, "Epic sadface: Password is required")
]

@pytest.mark.parametrize("user, password, result, error_message", test_data)
def test_write_you_name_text(open_base_page, user, password, result, error_message):
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
        error_button = page.locator('h3[data-test="error"]')
        expect(error_button).to_be_visible()
        expect(error_button).to_have_text(error_message)


