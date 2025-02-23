from playwright.sync_api import Page, expect


class ShoppingCartPage:

    def __init__(self, page: Page):
        self.page = page
        self.__checkout = page.locator("[data-test=\"checkout\"]")

    def push_checkout(self):
         self.__checkout.click()


