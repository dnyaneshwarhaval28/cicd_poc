from playwright.sync_api import expect


class OrderDetailsPage:

    def __init__(self, page):
        self.page = page

    def checkout_order(self):
        self.page.get_by_text("Checkout").click()
        expect(self.page.locator("input[id='country']")).to_be_visible()
        self.page.locator("#checkbox2").click()
        self.page.get_by_text("Purchase").click()
        self.verifyOrderMessage()

    def verifyOrderMessage(self):
        expect(self.page.locator("//div/strong")).to_contain_text("Success!")
