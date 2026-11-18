from playwright.sync_api import Page

class ActividadesPage:
    def __init__(self, page: Page):
        self.page = page
        
        # 1. Localizador del botón redondo naranja (+) de la primera fila
        self.primer_boton_inscribir = page.locator("table tbody tr").first.locator("button").first
        
        # 2. Botón "Confirmar Inscripción" del primer modal
        self.confirmar_inscripcion_btn = page.get_by_role("button", name="Confirmar Inscripción")
        
        # 3. Botón "INSCRIBIR" definitivo: filtramos estrictamente por el elemento modal activo (.cdk-overlay-container o div role dialog)
        # Esto ignora todos los botones "Inscribir" de la tabla de fondo
        self.inscribir_definitivo_btn = page.locator(".cdk-overlay-container, div[role='dialog']").get_by_role("button", name="INSCRIBIR", exact=True).or_(page.locator("button:has-text('INSCRIBIR')"))

    def inscribirse_a_primera_actividad(self):
        # 1. Esperamos y clickeamos el botón de la primera fila
        self.primer_boton_inscribir.wait_for(state="visible", timeout=10000)
        self.page.wait_for_timeout(1000)
        self.primer_boton_inscribir.click(force=True)
        
        # 2. Esperamos y confirmamos en el primer modal
        self.confirmar_inscripcion_btn.wait_for(state="visible", timeout=8000)
        self.confirmar_inscripcion_btn.click()
        
        # 3. Esperamos y clickeamos de forma quirúrgica el botón amarillo definitivo
        self.inscribir_definitivo_btn.last.wait_for(state="visible", timeout=5000)
        self.inscribir_definitivo_btn.last.click()
