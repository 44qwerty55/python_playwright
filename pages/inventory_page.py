from playwright.sync_api import Page, expect


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.__title_textfield = page.locator("[data-test=\"title\"]")
        self.__header = page.locator("[data-test=\"secondary-header\"]")
        self.__shopping_cart_badge = page.locator("[data-test=\"shopping-cart-badge\"]")
        self.__add_to_cart_sauce_labs_backpack = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.__add_to_cart_sauce_labs_bike_light = page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]")
        self.__add_to_cart_sauce_labs_fleece_jacket = page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]")
        self.__add_to_cart_sauce_labs_bolt_t_shirt = page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]")
        self.__add_to_cart_sauce_labs_onesie = page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]")
        self.__add_to_cart_t_short = page.locator("[data-test=\"add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)\"]")
        self.__push_shopping_cart = page.locator("[data-test=\"shopping-cart-link\"]")



    def validate_title(self, title: str):
        expect(self.__title_textfield).to_contain_text(title)

    def validate_snapshot(self, snapshot: str):
        expect(self.__header).to_match_aria_snapshot(snapshot)

    def validate_shopping_cart_badge(self, number_badge: int):
        expect(self.__shopping_cart_badge).to_contain_text(number_badge)

    def add_backpack_to_cart(self):
        self.__add_to_cart_sauce_labs_backpack.click()

    def add_bike_light_to_cart(self):
        self.__add_to_cart_sauce_labs_bike_light.click()

    def add_fleece_jacket_to_cart(self):
        self.__add_to_cart_sauce_labs_fleece_jacket.click()

    def add_bolt_t_shirt_to_cart(self):
        self.__add_to_cart_sauce_labs_bolt_t_shirt.click()

    def add_onesie_to_cart(self):
        self.__add_to_cart_sauce_labs_onesie.click()

    def add_to_cart_t_short(self):
         self.__add_to_cart_t_short.click()

    def push_shopping_cart(self):
        self.__push_shopping_cart.click()

    def add_all_items_to_cart(self):
        self.add_backpack_to_cart()
        self.add_bike_light_to_cart()
        self.add_fleece_jacket_to_cart()
        self.add_bolt_t_shirt_to_cart()
        self.add_onesie_to_cart()
        self.add_to_cart_t_short()

