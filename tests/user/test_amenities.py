import os
import re
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.sidebar_page import SidebarPage
from pages.amenities_page import AmenitiesPage

def test_apertura_modal_reserva_amenities(page):
    """
    [TC] AME-SC-01 - Validar la correcta apertura del formulario flotante para reservar un Amenity
    """
    # 1. Flujo de Login estándar
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_with_password(os.getenv("SOCIO_EMAIL"), os.getenv("SOCIO_PASSWORD"))

    sidebar_page = SidebarPage(page)
    amenities_page = AmenitiesPage(page)

    # 2. Navegar a la sección de Amenities desde la Sidebar
    sidebar_page.ir_a_amenities()
    expect(page).to_have_url(re.compile(r".*/amenities.*"), timeout=8000)

    # 3. Ejecutar la apertura del formulario de reserva
    amenities_page.abrir_modal_reserva()

    # 4. Verificación formal: Validamos que el cuadro de diálogo de reserva esté visible
    modal = page.get_by_role("dialog")
    expect(modal.first).to_be_visible(timeout=1000)

    # 5. Pausa de 2 segundos para observar visualmente la interfaz antes de que finalice el test
    page.wait_for_timeout(2000)
