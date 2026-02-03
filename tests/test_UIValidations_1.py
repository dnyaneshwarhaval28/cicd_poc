from playwright.sync_api import expect
from pageObjects.login import LoginPage

def test_UIValidationStaticScript(browserInstance):
    #iphone X, Nokia Edge, Blackberry -> verify 3 items are showing in cart.
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    ordersPage = loginPage.login("rahulshettyacademy","Learning@830$3mK2")

    ordersPage.select_product("iphone X")
    ordersPage.select_product("Nokia Edge")

    orderDetailsPage = ordersPage.select_checkout()
    expect(orderDetailsPage.page.locator(".media-body")).to_have_count(2)
    orderDetailsPage.checkout_order()