from playwright.sync_api import Page

class PerfilPage:
    def __init__(self, page: Page):
        self.page = page
        # Apuntamos quirúrgicamente al botón de envío de cambios
        self.guardar_cambios_btn = page.get_by_role("button", name="Guardar cambios")

    def guardar_perfil(self):
        # Esperamos que sea visible e interactivo y lo presionamos
        self.guardar_cambios_btn.wait_for(state="visible", timeout=10000)
        self.page.wait_for_timeout(1000)
        self.guardar_cambios_btn.click(force=True)
