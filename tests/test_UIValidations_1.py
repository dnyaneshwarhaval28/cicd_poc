from playwright.sync_api import expect
from pageObjects.login import LoginPage
import allure

@allure.title("Login Test")
@allure.description("Verify login functionality")
def test_UIValidationStaticScript(browserInstance):
    #iphone X, Nokia Edge, Blackberry -> verify 3 items are showing in cart.
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    ordersPage = loginPage.login("rahulshettyacademy","Learning@830$3mK2")

    ordersPage.select_product("iphone X")
    ordersPage.select_product("Nokia Edge")
    ordersPage.select_product("Blackberry")

    orderDetailsPage = ordersPage.select_checkout()
    expect(orderDetailsPage.page.locator(".media-body")).to_have_count(3)
    # orderDetailsPage.checkout_order()
    print("Successfull login")