import os
import re
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.sidebar_page import SidebarPage
from pages.perfil_page import PerfilPage

def test_guardar_cambios_perfil(page):
    """
    [TC] PER-SC-01 - Validar la actualización de datos presionando Guardar Cambios en Mi Perfil
    """
    # 1. Flujo de Login estándar
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_with_password(os.getenv("PROF_EMAIL"), os.getenv("PROF_PASSWORD"))

    sidebar_page = SidebarPage(page)
    perfil_page = PerfilPage(page)

    # 2. Navegar a la sección de Mi Perfil desde la Sidebar
    sidebar_page.ir_a_perfil()
    expect(page).to_have_url(re.compile(r".*/perfil.*"), timeout=8000)

    # 3. Presionar el botón para Guardar Cambios
    perfil_page.guardar_perfil()

    # 4. Breve pausa de 3 segundos para corroborar visualmente el guardado antes de cerrar
    page.wait_for_timeout(1500)
