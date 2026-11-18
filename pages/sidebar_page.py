from playwright.sync_api import Page

class SidebarPage:
    def __init__(self, page: Page):
        self.page = page
        self.actividades_link = page.get_by_role("link", name="Actividades", exact=True)
        self.certificados_link = page.get_by_role("link", name="Certificados", exact=True)
        self.grupo_familiar_link = page.get_by_role("link", name="Grupo familiar", exact=True)
        self.cuotas_link = page.get_by_role("link", name="Cuotas", exact=True)
        self.amenities_link = page.get_by_role("link", name="Amenities", exact=True)
        self.calendario_link = page.get_by_role("link", name="Mi calendario", exact=True)
        # Agregamos el localizador para Mi perfil basado en el menú
        self.perfil_link = page.get_by_role("link", name="Mi perfil", exact=True)

    def ir_a_actividades(self):
        self.actividades_link.wait_for(state="visible", timeout=5000)
        self.actividades_link.click()

    def ir_a_certificados(self):
        self.certificados_link.wait_for(state="visible", timeout=5000)
        self.certificados_link.click()

    def ir_a_grupo_familiar(self):
        self.grupo_familiar_link.wait_for(state="visible", timeout=5000)
        self.grupo_familiar_link.click()

    def ir_a_cuotas(self):
        self.cuotas_link.wait_for(state="visible", timeout=5000)
        self.cuotas_link.click()

    def ir_a_amenities(self):
        self.amenities_link.wait_for(state="visible", timeout=5000)
        self.amenities_link.click()

    def ir_a_calendario(self):
        self.calendario_link.wait_for(state="visible", timeout=5000)
        self.calendario_link.click()

    def ir_a_perfil(self):
        self.perfil_link.wait_for(state="visible", timeout=5000)
        self.perfil_link.click()
