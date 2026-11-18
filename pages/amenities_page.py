from playwright.sync_api import Page

class AmenitiesPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Localizamos el primer botón redondo de la columna Acciones en la tabla de Amenities
        self.primer_boton_reservar = page.locator("table tbody tr").first.locator("button").first
        
        # El título o elemento del modal que confirma que se abrió la interfaz de reserva
        self.titulo_modal = page.get_by_role("dialog").get_by_text("RESERVAR CANCHA").or_(page.get_by_text("RESERVAR CANCHA"))

    def abrir_modal_reserva(self):
        # 1. Esperamos a que la tabla y el botón de la primera fila estén listos
        self.primer_boton_reservar.wait_for(state="visible", timeout=10000)
        self.page.wait_for_timeout(1000)
        
        # 2. Hacemos click para desplegar el modal flotante
        self.primer_boton_reservar.click(force=True)
        
        # 3. Sincronizamos esperando que el título interno del diálogo aparezca en pantalla
        self.titulo_modal.first.wait_for(state="visible", timeout=8000)
        self.page.wait_for_timeout(1000)
