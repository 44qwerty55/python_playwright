from playwright.sync_api import Page, expect

from data.default_snapshots import CHECKOUT_COMPLETE_DEFAULT_SNAPSHOT


def test_emd_2_end_scenario(get_default_users, open_base_page, login_page, inventory_page, shopping_cart_page,
                            checkout_first_step_page, checkout_second_step_page, checkout_complete_page):
    user = get_default_users.get_standard_user()
    login_page.login_to_system(user.get_name(), user.get_password())
    inventory_page.add_all_items_to_cart()
    inventory_page.push_shopping_cart()
    shopping_cart_page.push_checkout()
    checkout_first_step_page.write_and_push_order("alex", "komanov", "20100")
    checkout_second_step_page.click_finish_button()
    checkout_complete_page.validate_pony_express()
    checkout_complete_page.validate_back_to_products()
    checkout_complete_page.validate_title("Checkout: Complete!")
    checkout_complete_page.validate_complete_header("Thank you for your order!")
    checkout_complete_page.validate_complete_text("Your order has been dispatched, and will arrive just as fast as the pony can get there!")
    checkout_complete_page.validate_snapshot(CHECKOUT_COMPLETE_DEFAULT_SNAPSHOT)