from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.switch_to_password_btn = page.get_by_text("usar tu contraseña", exact=False)
        self.email_input = page.locator("#auth-password-email")
        self.password_input = page.locator("input[type='password']")
        self.login_button = page.get_by_role("button", name="Ingresar")

    def navigate(self):
        self.page.goto("https://stg.blueopendata.com/bsports-club/login", wait_until="networkidle")

    def login_with_password(self, email: str, password: str):
        self.switch_to_password_btn.wait_for(state="visible", timeout=10000)
        self.switch_to_password_btn.click()
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
