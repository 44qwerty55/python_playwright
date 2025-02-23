from playwright.sync_api import Page, expect

def test_write_you_name_text(open_base_page):
    page = open_base_page
    page.wait_for_timeout(1000)
    select_element = page.locator('[id="developer-name"]')
    select_element.fill('Test Test')
    page.wait_for_timeout(1000)
    page.locator('[id="populate"]').click()

def test_select_features(open_base_page):
    page = open_base_page
    page.wait_for_timeout(1000)
    checkbox_features = page.get_by_role('checkbox', name='re-using')
    checkbox_features.check()
    page.wait_for_timeout(1000)
    checkbox_features.uncheck()

def test_select_test_cafe(open_base_page):
    page = open_base_page
    page.wait_for_timeout(1000)
    checkbox_test_cafe = page.get_by_role('checkbox', name='I have tried TestCafe')
   # expect(page.locator('[id="slider"]')).to_be_visible()
   # checkbox_test_cafe = page.locator('[id="tried-test-cafe"]')
    checkbox_test_cafe.click()
    page.wait_for_timeout(1000)
    expect(page.locator('[id="slider"]')).to_be_visible()
    #slider

