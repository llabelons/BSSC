import os
import re
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.sidebar_page import SidebarPage

def test_navegacion_seccion_cuotas(page):
    """
    [TC] CUO-SC-01 - Validar la navegación exitosa a la sección de Cuotas
    """
    # 1. Flujo de Login
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_with_password(os.getenv("SOCIO_EMAIL"), os.getenv("SOCIO_PASSWORD"))

    sidebar_page = SidebarPage(page)

    # 2. Navegar a la sección Cuotas desde la Sidebar
    sidebar_page.ir_a_cuotas()

    # 3. Verificación formal: Validamos que la URL haya cambiado correctamente
    expect(page).to_have_url(re.compile(r".*/cuotas.*"), timeout=8000)

    # 4. Mantener la interfaz visible por 3 segundos antes de finalizar
    page.wait_for_timeout(1000)
