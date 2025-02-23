import pytest
from playwright.sync_api import expect, Page

snapshot = "- text: Products Name (A to Z)\n- combobox:\n  - option \"Name (A to Z)\" [selected]\n  - option \"Name (Z to A)\"\n  - option \"Price (low to high)\"\n  - option \"Price (high to low)\""

test_data = [
    ("standard_user", "secret_sauce", snapshot),
    ("problem_user", "secret_sauce",  snapshot),
    ("performance_glitch_user", "secret_sauce", snapshot),
    ("error_user", "secret_sauce", snapshot),
    ("visual_user", "secret_sauce", snapshot),
]

@pytest.mark.parametrize("username, password, snapshot_page", test_data)
def test_login(login_page, inventory_page, open_base_page, username: str, password: str, snapshot_page: str):
    page = open_base_page
    login_page.login_to_system(username, password)

    expect(page).to_have_url('https://www.saucedemo.com/inventory.html')
    inventory_page.validate_title("Products")
    #page.wait_for_timeout(1000)
    expect(page.locator("[data-test=\"secondary-header\"]")).to_match_aria_snapshot(snapshot_page )

# expect(page).to_have_url(base_url)
   # expect(page).to_have_title("Swag Labs")


