from .dashboard import DashboardPage


class LoginPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    def login(self,userEmail,userPassword):
        self.page.get_by_label("Username:").fill(userEmail)
        self.page.get_by_label("Password:").fill(userPassword)
        self.page.get_by_role("combobox").select_option("teach")
        self.page.locator("#terms").check()
        self.page.get_by_role("button", name="Sign In").click()
        dashboardPage = DashboardPage(self.page)
        return dashboardPage
