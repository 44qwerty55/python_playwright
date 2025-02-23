from playwright.sync_api import Page, expect


class CheckoutSecondStepPage:

    def __init__(self, page: Page):
        self.page = page
        self.__finish_button = page.locator("[data-test=\"finish\"]")

    def click_finish_button(self):
        self.__finish_button.click()

