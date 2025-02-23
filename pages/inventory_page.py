from playwright.sync_api import Page, expect


class InventoryPage:

    def __init__(self, page: Page):
        self.__title_textfield = page.locator("[data-test=\"title\"]")
        self.__header = page.locator("[data-test=\"secondary-header\"]")
        self.__shopping_cart_badge = page.locator("[data-test=\"shopping-cart-badge\"]")


    def validate_title(self, title: str):
        expect(self.__title_textfield).to_contain_text(title)

    def validate_snapshot(self, snapshot: str):
        expect(self.__header).to_match_aria_snapshot(snapshot)

    def validate_shopping_cart_badge(self, number_badge: int):
        expect(self.__shopping_cart_badge).to_contain_text(number_badge)
