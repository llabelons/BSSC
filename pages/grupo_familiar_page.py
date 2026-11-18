from playwright.sync_api import Page

class GrupoFamiliarPage:
    def __init__(self, page: Page):
        self.page = page
        # Buscamos el botón superior derecho de forma exacta
        self.agregar_familiar_btn = page.get_by_role("button", name="AGREGAR FAMILIAR").or_(page.locator("button:has-text('AGREGAR FAMILIAR')"))
        # El título interno que se renderiza obligatoriamente al abrir la ventana flotante
        self.titulo_modal = page.get_by_role("heading", name="AGREGAR FAMILIAR").or_(page.get_by_text("COMPLETA LOS DATOS PARA SOLICITAR"))

    def abrir_formulario(self):
        # 1. Esperamos el botón y lo clickeamos
        self.agregar_familiar_btn.wait_for(state="visible", timeout=10000)
        self.page.wait_for_timeout(1000)
        self.agregar_familiar_btn.click(force=True)
        
        # 2. Sincronización exacta: Esperamos que aparezca el título interno del modal en la pantalla
        self.titulo_modal.first.wait_for(state="visible", timeout=8000)
        self.page.wait_for_timeout(1000)
