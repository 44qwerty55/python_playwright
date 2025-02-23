from playwright.sync_api import Page, expect


class CheckoutCompletePage:

    def __init__(self, page: Page):
        self.page = page
        self.__pony_express = page.locator("[data-test=\"pony-express\"]")
        self.__back_to_products = page.locator("[data-test=\"back-to-products\"]")
        self.__title = page.locator("[data-test=\"title\"]")
        self.__complete_header = page.locator("[data-test=\"complete-header\"]")
        self.__complete_text = page.locator("[data-test=\"complete-text\"]")
        self.__primary_header = page.locator("[data-test=\"primary-header\"]")

    def validate_pony_express(self):
        expect(self.__pony_express).to_be_visible()

    def validate_back_to_products(self):
        expect(self.__back_to_products).to_be_visible()

    def validate_title(self, text: str):
        expect(self.__title).to_contain_text(text)

    def validate_complete_header(self, text: str):
        expect(self.__complete_header).to_contain_text(text)

    def validate_complete_text(self, text: str):
        expect(self.__complete_text).to_contain_text(text)

    def validate_snapshot(self, snapshot: str):
        expect(self.__primary_header).to_match_aria_snapshot(snapshot)