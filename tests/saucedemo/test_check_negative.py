import pytest
from playwright.sync_api import expect

test_data = [
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("visual_user", "another_value", "Epic sadface: Username and password do not match any user in this service"),
    ("visual_user", "", "Epic sadface: Password is required"),
    ("", "secret_sauce", "Epic sadface: Username is required"),
]

@pytest.mark.parametrize("user, password, error_message", test_data)
def test_login(open_base_page, user, password, error_message):
    page = open_base_page
    select_user_name_element = page.locator('[id="user-name"]')
    select_user_name_element.fill(user)
    select_user_pass_element = page.locator('[id="password"]')
    select_user_pass_element.fill(password)
    button = page.get_by_role('button', name='Login')
    button.click()
    page.wait_for_timeout(1000)

    page.wait_for_url(page.url)
    error_button = page.locator('h3[data-test="error"]')
    expect(error_button).to_be_visible()
    expect(error_button).to_have_text(error_message)


