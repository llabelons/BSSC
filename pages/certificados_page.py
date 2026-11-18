from playwright.sync_api import Page

class CertificadosPage:
    def __init__(self, page: Page):
        self.page = page
        
        # El área de arrastrar archivo suele ser un elemento de tipo 'input[type="file"]' oculto internamente.
        # Playwright permite interactuar directamente con él usando set_input_files.
        self.file_input = page.locator("input[type='file']")
        
        # El botón naranja definitivo para confirmar la subida
        self.subir_certificado_btn = page.get_by_role("button", name="Subir certificado")

    def cargar_y_subir_certificado(self, archivo_path: str):
        # 1. Subimos el archivo directamente al input de Playwright (esto simula seleccionarlo y darle a "Abrir")
        self.file_input.wait_for(state="attached", timeout=10000)
        self.file_input.set_input_files(archivo_path)
        
        # 2. Le damos un segundo de respiro para que impacte en la interfaz el texto "Archivo seleccionado: certificado.png"
        self.page.wait_for_timeout(1000)
        
        # 3. Clickeamos en "Subir certificado"
        self.subir_certificado_btn.wait_for(state="visible", timeout=5000)
        self.subir_certificado_btn.click()
