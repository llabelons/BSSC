from playwright.sync_api import Page

class CredencialPage:
    def __init__(self, page: Page):
        self.page = page
        self.ver_qr_button = page.get_by_text("Ver QR")
        self.qr_code_element = page.locator("canvas, img, qrcode")
        # Localizamos el botón "Volver" del modal del QR
        self.volver_button = page.get_by_role("button", name="Volver")

    def mostrar_qr(self):
        self.ver_qr_button.wait_for(state="visible", timeout=12000)
        self.page.wait_for_timeout(1000)
        self.ver_qr_button.click(force=True)

    def cerrar_qr(self):
        # Esperamos que el botón Volver sea interactivo y lo clickeamos
        self.volver_button.wait_for(state="visible", timeout=5000)
        self.volver_button.click()
