from playwright.sync_api import Page, expect


class CheckoutFirstStepPage:

    def __init__(self, page: Page):
        self.page = page
        self.__first_name_textfield = page.locator("[data-test=\"firstName\"]")
        self.__last_name_textfield = page.locator("[data-test=\"lastName\"]")
        self.__postal_code_textfield = page.locator("[data-test=\"postalCode\"]")
        self.__continue_button = page.locator("[data-test=\"continue\"]")

    def type_first_name(self, first_name: str):
        self.__first_name_textfield.fill(first_name)

    def type_last_name(self, last_name: str):
        self.__last_name_textfield.fill(last_name)

    def type_postal_code(self, postal_code: str):
        self.__postal_code_textfield.fill(postal_code)

    def click_continue_button(self):
        self.__continue_button.click()

    def write_and_push_order(self, first_name: str, last_name: str, code: str):
        self.type_first_name(first_name)
        self.type_last_name(last_name)
        self.type_postal_code(code)
        self.click_continue_button()