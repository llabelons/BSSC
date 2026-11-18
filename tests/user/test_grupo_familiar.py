import os
import re
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.sidebar_page import SidebarPage
from pages.grupo_familiar_page import GrupoFamiliarPage

def test_apertura_modal_agregar_familiar(page):
    """
    [TC] FAM-SC-01 - Validar la correcta apertura del modal Agregar Familiar
    """
    # 1. Flujo de Login
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_with_password(os.getenv("SOCIO_EMAIL"), os.getenv("SOCIO_PASSWORD"))

    sidebar_page = SidebarPage(page)
    grupo_familiar_page = GrupoFamiliarPage(page)

    # 2. Navegar a la sección Grupo Familiar
    sidebar_page.ir_a_grupo_familiar()
    expect(page).to_have_url(re.compile(r".*/grupo-familiar.*"), timeout=8000)

    # 3. Abrir el formulario flotante
    grupo_familiar_page.abrir_formulario()

    # 4. Verificación formal basada en el Aria snapshot real de la app
    modal = page.get_by_role("dialog", name="Agregar familiar")
    expect(modal).to_be_visible(timeout=5000)

    # 5. Pausa de 5 segundos para comprobar la interfaz visualmente antes de cerrar
    page.wait_for_timeout(1000)
